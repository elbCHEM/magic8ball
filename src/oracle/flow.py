from oracle.logic import get_answer


MAX_QUESTIONS = 100
PROMPT_STRING_FIRST_ITERATION = "Please enter a question - (Exit to returning quit): "
PROMPT_STRING_LATER_ITERATION = "Please enter a another question - (Exit to returning quit): "
PROPER_EXIT_STRING = 'Please come back another time.'


class TooManyQuestionAsked(Exception):
    questions_asked: int

    def __init__(self, questions_asked: int, *args: object) -> None:
        self.questions_asked = questions_asked
        super().__init__(*args)


def main() -> None:
    try:
        app_flow()
        print(PROPER_EXIT_STRING, end='\n')
    except TooManyQuestionAsked:
        print("Too many questions asked. Please try again later")
    except KeyboardInterrupt:
        print('Process terminated due to keyboard interrupt')


def app_flow() -> None:
    print("Welcome. I am the oracle. I will answer all question. Please beware, you way not like what you hear.", end='\n\n')

    for n in range(1, MAX_QUESTIONS+1):
        userinput = input(PROMPT_STRING_FIRST_ITERATION if n == 0 else PROMPT_STRING_LATER_ITERATION).strip()
        if not userinput or userinput.lower() == 'quit':
            return
        if not isvalid(userinput):
            print("Sorry! Invalid question detected.", end='\n\n')
            continue
        print(f"The answer to your question is: \"{get_answer()}\"", end='\n\n')

    raise TooManyQuestionAsked(n)


# To-Do: Make a proper validator
def isvalid(_: str) -> bool:
    return True


if __name__ == '__main__':
    main()
