__author__ = 'patrickh'
print 'Hello World!'

def main():
    try:
        print 1 + 'hello'
    except:
        print ' we failed'
    print 'hello we continued with script'

main()

def rain():
    try:
        print 1 + 'hello'
    except Exception, e:
        print str(e)

    print 'script continues'

rain()
