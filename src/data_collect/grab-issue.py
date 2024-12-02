import requests
import json
import csv
import timeModel
import redis
import threading
import signal

r = redis.Redis(host='localhost', port=6379, db=0)

flag = True

def sanitize_text(s):
    if s is None:
        return ""
    if type(s) is not str:
        s = str(s)
    s1 = s.split('\n')
    s2 = s1[0].split(',')
    if len(s1) > 1 or len(s2) > 1:
        return s2[0] + "..."
    else:
        return s2[0]

def grab_all_issue(token):
    global flag
    while flag and r.scard('commit_target') > 0:
        repo = r.spop('commit_target').decode('utf-8')
        oc = r.get(repo).decode('utf-8')

        csvfile = open(f'data/issue/{oc}.csv', 'a')
        csvwriter = csv.writer(csvfile)
        if csvfile.tell() == 0:
            csvwriter.writerow(['Repo', 'Status', 'Date', 'Close Date'])

        url = f"https://api.github.com/repos/{repo}/issues"
        current = 1

        while True:
            headers = {
                'Authorization': f"Bearer {token}",
                'Content-Type': 'application/json'
            }
            try:
                response = requests.get(url, headers=headers, params={'per_page': 100, 'page': current, 'since': '2022-08-01T00:00:00Z', 'until': '2024-08-31T23:59:59Z'})
                if response.status_code != 200:
                    print(response)
                    print(f"retrying {repo} for {current} page...")
                    time.sleep(1)
                    continue
                data = response.json()
                for issue in data:
                    try:
                        status = issue['state']
                        date = issue['created_at']
                        close_date = issue['closed_at']
                        csvfile.write(f"{repo},{status},{date},{close_date}\n")
                    except:
                        continue
                if len(data) == 0:
                    break
                current += 1
            except Exception as e:
                print(f"retrying {repo}...")
                continue
        print(f"Finish to crawl {repo}")

def custom_signal_handler(sig, frame):
    global flag
    flag = False

tokens = json.load(open('tokens.json', 'r'))

def main():
  signal.signal(signal.SIGINT, custom_signal_handler)
  t = []
  for i in range(len(tokens)):
    t.append(threading.Thread(target=grab_all_issue, args=(tokens[i], )))
    t[i].start()
  
  for i in range(len(tokens)):
    t[i].join()

if __name__ == "__main__":
  main()