import smtplib
import datetime
import email
import report_tool


def mail_send():
    fromaddr = "from@gmail.com"
    toaddr = "to@gmail.com"

    msg = email.mime.multipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log Report"

    body = "Log Report : " + datetime.datetime.now().strftime("%Y/%m/%d")

    msg.attach(email.mime.text(body, 'plain'))
    filename = [report_tool.file_list]
    attachment = open(filename, "rb")

    part = email.mime.multipart('application', 'octet-stream')
    part.set_payload((attachment).read())
    email.encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()