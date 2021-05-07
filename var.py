from main_startup.core.decorators import friday_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text, edit_or_send_as_file
import calendar
from datetime import datetime


@borg.on(admin_cmd(outgoing=True, pattern="utime(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?"))
@bot.on(
    sudo_cmd(
        outgoing=True,
        pattern="utime(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?",
        allow_sudo=True,
     )
 )
async def _d(client, message):
    year_ = datetime.now().year
    date_ = datetime.now().day
    month_ = datetime.now().month
    mydate = datetime.now()
    da = mydate.strftime("Date : %d \nMonth : %B \nYear : %Y")
    dt = mydate.strftime("Hour : %H \nMinute : %M")
    cal_ = calendar.month(year_, month_)
    f_d = f"<code>{cal_}\n{da} \n\n{dt}</code>"
    await edit_or_reply(message, f_d, parse_mode="html")
