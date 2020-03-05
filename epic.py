"""
theatername = "Epic Theatres of Ocala"
theaterstreet = "4414 SW College Road"
theatercity = "Ocala, FL 34474"
theatrephone = "(386)736-6830"

Find theatername\r
Replace ""

Find theaterstreet\r
Replace ""

Find theatercity\r
Replace ""

Find theaterphone\r
Replace ""

date = %m/%d/%y
weekday = weekday
datetext = March 6


Find "Showtimes for Friday, March 6"
Replace "location\tEpic Theatres of Ocala\t"

Find "\r\r"
Replace "location\tEpic Theatres of Ocala\t"

Find "(:\d\d)pm, "
Replace "$1p | "

Find "(:\d\d)am, "
Replace "$1a | "

Find " - \d hr. \d+? mins.\r"
Replace "\t"

Find "pm\r"
Replace "\t"

movie_format1 = "Closed Captioning; Descriptive Narration; Hearing Impaired; Luxury Recliner; Reserved Seating; XL"
movie_format2 = "Closed Captioning; Descriptive Narration; Hearing Impaired; Luxury Recliner; Reserved Seating"

Find movie_format1
Replace "XL\tsynopsis\tdate\tOcala, FL"

Find movie_format2
Replace "Standard\tsynopsis\tdate\tOcala, FL"

Find " ("
Replace "\t"

Find ")"
Replace ""

"""
