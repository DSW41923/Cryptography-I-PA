from PA import split_by_length, strxor

import urllib2

TARGET = 'http://crypto-class.appspot.com/po?er='
CT = 'f20bdba6ff29eed7b046d1df9fb70000' + '58b1ffb4210a580f748b4ac714c001bd' + \
    '4a61044426fb515dad3f21f18aa577c0' + 'bdf302936266926ff37dbf7035d5eeb4'

# --------------------------------------------------------------
# padding oracle
# --------------------------------------------------------------


class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
            # import pdb; pdb.set_trace()
        except urllib2.HTTPError, e:
            print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True  # good padding
            return False  # bad padding


decoded_CT = CT.decode('hex')
split_CT = split_by_length(decoded_CT, 16)
byte_num = len(split_CT)
split_MSG = [[]] * byte_num
po = PaddingOracle()
for i in range(1, byte_num):
    IV = split_CT[i - 1]
    part_MSG = [''] * 16
    for j in range(1, 17):
        print j
        for k in range(256):
            if i == 3 and k == 1:
                continue
            print k
            trial = strxor(chr(k) + ''.join(part_MSG[-j:]), chr(j) * j)
            trial_CT = IV[:-j] + strxor(IV[-j:], trial) + split_CT[i]
            trial_CT = trial_CT.encode('hex')
            # print trial_CT
            if po.query(trial_CT):       # Issue HTTP query with the given argument
                part_MSG[-j] = chr(k)
                print j, k, chr(k)
                break
            else:
                continue
    split_MSG[i] = part_MSG
print ''.join([''.join(s) for s in split_MSG])
