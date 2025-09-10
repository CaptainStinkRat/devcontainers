from alive_progress import alive_bar

with alive_bar(100) as progressBar:
    for x in range(100):
        sleep(0.02)
        progressBar()
