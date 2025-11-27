# The file start_times.csv contains individual start times for a programming exam, in the format name;hh:mm. An example:

# jarmo;09:00
# timo;18:42
# kalle;13:23

# Additionally, the file submissions.csv contains points and handin times for individual exercises. The format here is name;task;points;hh:mm. An example:

# jarmo;1;8;16:05
# timo;2;10;21:22
# jarmo;2;10;19:15
# jne...

# Your task is to find the students who spent over 3 hours on the exam tasks. That is, any student whose any task was handed in over 3 hours later than their exam start time is labelled a cheater. There may be more than one submission for the same task for each student. You may assume all times are within the same day.

# Please write a function named cheaters(), which returns a list containing the names of the students who cheated

import csv, datetime

def cheaters():
    with open("start_times.csv") as start_times, open("submissions.csv") as submissions:
        exam_dict = {}
        for exam_line in csv.reader(start_times, delimiter=";"):
            exam_dict[exam_line[0]] = exam_line[1]
        # print(exam_dict)
# bir kuple: {'matti': '13:33', 'erkki': '15:13', 'antti': '15:49', 'emilia': '13:37', 'henrik': '15:01'}

        submissions_list = []
        for submission_line in csv.reader(submissions, delimiter=";"):
            submission_list = []
            submission_list.append(submission_line[0])
            submission_list.append(submission_line[1])
            submission_list.append(submission_line[2])
            submission_list.append(submission_line[3])
            submissions_list.append(submission_list)
        print(submissions_list)
# bir kuple: [['arto', '1', '4', '19:12'], ['erkki', '2', '2', '16:03'], ['matti', '7', '3', '16:21'], ['jyrki', '1', '3', '17:43']]

        cheater_list = []
        limit = datetime.timedelta(hours=3)
        # print(limit)
        for name, start_time in exam_dict.items():
            start_time_list = start_time.split(":")
            start = datetime.datetime(1900, 1, 1, int(start_time_list[0]), int(start_time_list[1]))
            for submission in submissions_list:
                if name not in cheater_list: #aynı kisiyi birden fazla eklememek icin
                    if name == submission[0]: #alt: if name not in cheater_list and name == submission[0]:
                        submission_time = submission[3].split(":")
                        submission = datetime.datetime(1900, 1, 1, int(submission_time[0]), int(submission_time[1]))
                        diff = submission - start
                        # print(diff)
                        if diff > limit:
                            cheater_list.append(name)
        return cheater_list            

if __name__ == "__main__":
    print(cheaters())


# alt2 - mooc.fi: cok daha verimli (Yukarıdaki M*N yerine M+N)
import csv
from datetime import datetime, timedelta

def cheaters():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time

        # Then read submissions
        # From each student, last (i.e. greatest) is saved
        submission_times = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[3], "%H:%M")
            # If name does not exists in dictionary, add time directly to the dictionary
            if name not in submission_times:
                submission_times[name] = time
            # If there alredy exists time for key, compare if current time is greater
            elif time > submission_times[name]:
                submission_times[name] = time
            
    # print(len(start_times) == len(submission_times)) #true
    cheaters = []
    # Iterate through students one by one
    for name in start_times: # **aynı fonksiyonda tum degiskenler erisilebilir**
        if submission_times[name] - start_times[name] > timedelta(hours=3):
            # print(f"{submission_times[name]} - {start_times[name]} = {submission_times[name] - start_times[name]}")
            # print(timedelta(hours=3))
            cheaters.append(name)
    return cheaters

if __name__ == "__main__":
    print(cheaters())


# alt3 - glm 4.6 revizyonu: yukarıdaki kodun daha iyisi:
import csv
from datetime import datetime, timedelta

def _read_start_times(file_path: str) -> dict:
    """Başlangıç zamanlarını bir CSV dosyasından okur ve bir sözlüğe dönüştürür."""
    start_times = {}
    with open(file_path) as f:
        # 'row' değişkeni artık sadece bu fonksiyonun kapsamında yaşar.
        for row in csv.reader(f, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
    return start_times

def _get_latest_submission_times(file_path: str) -> dict:
    """Gönderileri okur ve her öğrenci için en son gönderim zamanını döndürür."""
    submission_times = {}
    with open(file_path) as f:
        # 'row' değişkeni de sadece bu fonksiyonun kapsamında yaşar.
        for row in csv.reader(f, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[3], "%H:%M")
            
            # Her öğrenci için sadece en geç zamanı sakla
            if name not in submission_times or time > submission_times[name]:
                submission_times[name] = time
    return submission_times

def cheaters():
    """
    Herhangi bir görevi sınav başlangıcından 3 saatten sonra teslim eden öğrencileri bulur.
    """
    # Ana mantık artık çok temiz ve okunabilir
    start_times = _read_start_times("start_times.csv")
    submission_times = _get_latest_submission_times("submissions.csv")

    cheaters_list = []
    for name, start_time in start_times.items():
        # Daha sağlam bir kod için, öğrencinin gönderisi olup olmadığını kontrol et
        if name in submission_times:
            if submission_times[name] - start_time > timedelta(hours=3):
                cheaters_list.append(name)
    
    return cheaters_list

if __name__ == "__main__":
    print(cheaters())
