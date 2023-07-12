import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

#_, PROJECT_ID = google.auth.default()
TASK_INDEX = int(os.environ.get("CLOUD_RUN_TASK_INDEX", 0))
TASK_COUNT = int(os.environ.get("CLOUD_RUN_TASK_COUNT", 1))
CANDIDATES = os.environ.get("CANDIDATES", '')

# purposely slow
def is_prime(num):

    if num == 1:
        print(num, "is not a prime number")
        return None
    elif num > 1:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
        else:
            print(num,"is a prime number")
            return True
        
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num,"is not a prime number")
        return None

def main():
    num = int(CANDIDATES.split(",")[TASK_INDEX])
    print(f'Determining if {num} is prime')
    print(is_prime(num))

if __name__ == "__main__":
    main()