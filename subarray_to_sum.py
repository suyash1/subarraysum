from collections import OrderedDict
import itertools

def sumfinder(arr, num):
    d = OrderedDict()
    processed = [0] * num
    for i in arr[::-1]:
        if i == num:
            print [num]
            break
        elif i > num:
            pass
        else:
            # if not processed[i]:
                print 'going in for i = ', i
                processed[i] = 1
                ith_index = arr.index(i)
                # temp = num
                l = []
                found_pair = True
                #for  j in arr[ith_index::-1]:
                j = i
                diff = num - j
                if diff in arr and found_pair and diff != j:
                    processed[diff] = 1
                    d[i] = [i, diff]
                    # break
                else:
                    found_pair = False
                    l.append(j)
                    processed[j] = 1
                    # print 'in else...diff is ', diff
                    for k in arr[arr.index(j)-1::-1]:
                        if arr.index(j)-1 < 0:
                            break
                        if diff - k in arr:
                            diff -= k
                            # print 'new diff is ', diff
                            if int(diff) in arr or not diff:
                                l.append(k) if not k in l else ''
                                l.append(diff) if diff and not diff in l else ''
                                processed[k] = 1
                                processed[diff] = 1
                                print l
                            if not diff:
                                break
                if sum(l) == num:
                    d[i] = l
                    break

    results = []
    for v in d.itervalues():
        # if sorted(v) not in results:
        results.append(sorted(list(set(v)))) if sum(list(set(v))) == num else ''
    # results.sort()
    print list(r for r,_ in itertools.groupby(results))
    return


if __name__ == '__main__':
    arr = [2, 4, 6, 8, 16, 32]
    sumfinder(arr, 14)
