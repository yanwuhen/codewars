def format_duration(seconds):
    if seconds == 0:
        return "now"
    s = seconds % 60
    m = seconds / 60
    h = m / 60
    m = m % 60
    d = h / 24
    h = h % 24
    y = d / 365
    d = d % 365
    l = []
    if y != 0:
        l.append("%d year" % y + 's'*(0 if y==1 else 1))
    if d != 0:
        l.append("%d day" % d + 's'*(0 if d==1 else 1))
    if h != 0:
        l.append("%d hour" % h + 's'*(0 if h==1 else 1))
    if m != 0:
        l.append("%d minute" % m + 's'*(0 if m==1 else 1))
    if s != 0:
        l.append("%d second" % s + 's'*(0 if s==1 else 1))
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return l[0] + " and " + l[1]
    return ", ".join(l[:-1])+ " and " + l[-1]

if __name__ == '__main__':
    def test(a, b):
        if a == b:
            print("right")
        else:
            print(a, "is not equal", b)
    test(format_duration(1), "1 second")
    test(format_duration(62), "1 minute and 2 seconds")
    test(format_duration(120), "2 minutes")
    test(format_duration(3600), "1 hour")
    test(format_duration(3662), "1 hour, 1 minute and 2 seconds")