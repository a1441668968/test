whitesps = '\r\n\v\f\t'


def rmlsp(lastr):
    for i in range(len(lastr)):
        if lastr[i] not in whitesps:
            return lastr[i:]
        else:
            return ''


lastr = input()
print(rmlsp(lastr))


####################################################
def bqbj(qs, js):
    for gj in range(0, qs // 5 + 1):
        for mj in range(0, (qs - 5 * gj) // 3 + 1):
            for xj in range(0, qs - 5 * gj - 3 * mj + 1):
                if qs - 5 * gj - 3 * mj - xj:
                    continue
                else:
                    if gj + mj + xj * 3 == js:
                        print('公鸡%s只,母鸡%s只,小鸡%s只' % (gj, mj, xj * 3))
                    else:
                        continue


bqbj(100, 100)
##########################################################
