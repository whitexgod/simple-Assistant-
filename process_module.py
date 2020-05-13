from output_module import output
from time_module import get_time,get_date
from input_module import take_input
from database import *
from internet import check_internet_connection,check_on_wiki,from_internet
from web import *
from quit import quit
import assistant_details


def process(query):

    if 'hi' in query :
        return "hello, Sir"
    elif 'hello' in query:
        return "Hi, Sir"
    elif "how are you" in query:
        return "I am fine sir, How are you doing?"
    elif "fine" in query:
        return "okay. What can i do for you sir."
    elif "thanks" in query:
        return "welcome, Sir"
    elif "thank you" in query:
        return "welcome, Sir"
    elif "welcome" in query:
        return "hehe, Sir you are a nice person"
    elif "are you a girl" in query:
        return "what do you think, sir"
    elif "girl" in query:
        return "sir, you are very smart"
    elif "i think you are a girl" in query:
        return "i have no doubt, sir"
    elif "boy" in query:
        return "Sir, i am a girl"
    elif "i think you are a boy" in query:
        return "Nice joke sir, but it was not funny"
    elif "sorry" in query:
        return "its ok, i never mind"
    elif "who is your creator" in query:
        return "My creator is Lord Tuhin Mukherjee"
    elif "ok" in query:
        return "its nice to talk with you, Sir"
    elif "okay" in query:
        return "its nice to talk with you, Sir"
    elif "ok i got it" in query:
        return "its nice to talk with you, Sir"
    elif "okay i got it" in query:
        return "its nice to talk with you, Sir"

    else:

        answer = get_answer_from_memory(query)

        if answer == "get time details" :
            return ("Time is "+ get_time())

        elif answer == 'quit':
            return ("Good-bye, Sir"+quit())

        elif answer== "check internet connection":
            if check_internet_connection():
                return "Internet is Connected"
            else:
                return "Internet is not Connected"

        elif answer == "tell date":
            return "Date is "+ get_date()

        elif answer == "on speak" :
            return turn_on_speech()

        elif answer == "off speak":
            return turn_off_speech()

        elif answer == "open facebook":
            open_facebook()
            return "opening facebook now"

        elif answer == "open google":
            open_google()
            return "opening google now"

        elif answer == "open browser":
            open_google()
            return "opening browser now"

        elif answer == "close browser":
            close_browser()
            return "Browser closed."

        elif answer == "change name":
            output("Okay! what do you want call me?")
            temp = take_input()
            if temp == assistant_details.name:
                return "Can't change. Its just my previous name"
            else:
                update_name(temp)
                assistant_details.name=temp
                return ("Now you can call me " + temp)


        else:

            output("Don't know this one. Should i search in wikipedia or in Internet?")
            ans = take_input()
            ans.lower()
            if "wikipedia" in ans:
                answer = check_on_wiki(query)
                if answer != "":
                    return answer

            elif "internet" in ans :
                answer = from_internet(query)
                if answer != "":
                    return answer



            else:

                output("Can you please tell me what it means?")
                ans=take_input()
                if "it means" in ans:
                    ans = ans.replace("it means","")
                    ans=ans.strip()

                    value=get_answer_from_memory(ans)
                    if value=="":
                        return ("Can't help with this one")

                    else:
                        inset_question_and_answer(query, value)
                        return ("Thanks, I will remember it for the next time")

                else:

                    return "Can't help with this one!"
