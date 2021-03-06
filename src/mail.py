from googleSheet import get_report_info
from reportInfo import *
from seminarDate import nextWednesdayDateUA

heading = """
<div style="height:100%;margin:0;padding:0;width:100%;background-color:#fafafa">
        <center>
            <table id="m_8632786949691406836bodyTable" style="height:100%;border-collapse:collapse;margin:0;padding:0;width:100%;background-color:#fafafa" width="100%" cellspacing="0" cellpadding="0" border="0" align="center">
                <tbody><tr>
                    <td id="m_8632786949691406836bodyCell" style="height:100%;margin:0;padding:10px;width:100%;border-top:0" valign="top" align="center">


                        <table style="border-collapse:collapse;border:0;max-width:600px!important" width="100%" cellspacing="0" cellpadding="0" border="0">
                            <tbody><tr>
                                <td id="m_8632786949691406836templatePreheader" style="background-color:#fafafa;background-image:none;background-repeat:no-repeat;background-position:center;background-size:cover;border-top:0;border-bottom:0;padding-top:9px;padding-bottom:9px" valign="top">
                                    <img src="cid:light.png" width="865" height="289">
                                </td>   
                            </tr>
                            <tr>
                                <td id="m_8632786949691406836templateHeader" style="background-color:#ffffff;background-image:none;background-repeat:no-repeat;background-position:center;background-size:cover;border-top:0;border-bottom:0;padding-top:9px;padding-bottom:0" valign="top">
                                    <table style="min-width:100%;border-collapse:collapse" width="100%" cellspacing="0" cellpadding="0" border="0">
                                        <tbody>
                                        <tr>
                                            <td style="padding-top:9px" valign="top">



                                                <table style="max-width:100%;min-width:100%;border-collapse:collapse" width="100%" cellspacing="0" cellpadding="0" border="0" align="left">
                                                    <tbody>
                                                    <tr>
                                                        <td style="padding-top:0;padding-right:18px;padding-bottom:9px;padding-left:18px;word-break:break-word;color:#202020;font-family:Helvetica;font-size:16px;line-height:150%;text-align:left" valign="top">
                                                            <center><i>You can find an english version of this announcement in the attachment to this message</i></center>
                                                            <p>Шановні колеги!&nbsp;</p>                                                   
                                                            <p>Запрошуємо Вас на черговий робочий семінар Центру дослідження даних Київського академічного університету.</p>
                                                            <ul>
"""

ending = """
<p><b>Де:</b> <a href="https://us02web.zoom.us/j/84322131944?pwd=a2pwRVFkWUsvdWRyRUdqNHZTNmNtZz09">конференція в Zoom</a></p>
<p><b>Meeting ID:</b> 843 2213 1944</p>
<p><b>Passcode:</b> 281615</p>
                                                            <p>За оновленою інформацією слідкуйте на сайті
                                                                <a href="https://sites.google.com/view/data-analysis/home">ЦДД КАУ</a>,
                                                                або на сторінці <a href="https://kau.org.ua/deps/math/251-seminar-tsentru-doslidzhennia-danykh-ta-innovatsii"> кафедри математики KAU.</a></p>
                                                                <p>Також інформація про оновлені семінари розташовується на сайті 
                                                                    <a href="https://www.imath.kiev.ua/events/index.php?seminarId=96">Інституту математики НАН України</a></p>
                                                            <p>
                                                                З повагою,
                                                            </p>
                                                            <p>
                                                                Керівники семінару: <br/>
                                                                Антонюк Олександра Вікторівна,<br/>
                                                                Сенько Іван Олександрович,<br/>
                                                                Ситник Дмитро Олексійович
                                                            </p>
                                                            <p>
                                                                Наукові секретарі семінару: <br/>
                                                                Максим Шамрай,<br/>
                                                                Марина Караванська
                                                            </p>
                                                        </td>
                                                    </tr>
                                                    </tbody>
                                                </table>


                                            </td>
                                        </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody></table>


                    </td>
                </tr>
            </tbody></table>
        </center>
        </div>
"""

def create_message():
    infoes = get_report_info()
    when = "</li></ul><p><b>Коли:</b> " + nextWednesdayDateUA + " (середа) о 17:00</p>"
    html = ""
    for info in infoes:
        html += ("""
            <li><p><b>Доповідач:</b> %s
                <br/>
                (""" % info.reporter) + (info.degree + ', ') * (info.degree != '') + \
        """%s)
            </p>
            <p><b>Тема:</b> %s </p>
            <p> %s </p>
        """ % (info.place, info.title, info.abstract)
    html = heading + html + when + ending
    return html