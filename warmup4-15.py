"""
Creating two classes, an employee and a job, where the employee class has-a job class.
When printing an instance of the employee object the output should look something like this:

My name is Morgan Williams, I am 24 years old and I am a Software Developer.
"""


class Job(object):
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary


class Employee(object):
    def __init__(self, name, age, job_title, job_salary):
        self.name = name
        self.age = age
        self.job = Job(job_title, job_salary)

    def __str__(self):
        return "Hi my name is %s, I am %s Years old and I am a %s, making $%i per year." \
               % (self.name, self.age, self.job.title, self.job.salary)

    # def speak(self):
    #     print "Hi my name is %s, I am %s Years old and I am a %s, making $%i per year." \
    #           % (self.name, self.age, self.job.title, self.job.salary)


morgan = Employee("Morgan Williams", 24, "Software Developer", 60000)

print morgan
# morgan.speak()