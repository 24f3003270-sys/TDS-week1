def is_prime(n):
  """Checks if a number is a prime number."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def find_nth_prime(n):
    """Finds the nth prime number."""
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1

if __name__ == "__main__":
    prime_to_find = 22
    twenty_second_prime = find_nth_prime(prime_to_find)
    print(f"The {prime_to_find}nd prime number is: {twenty_second_prime}")