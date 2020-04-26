#!/usr/bin/env python3
from Block import BlockChain


def main():
    print(u"\nTesting Blockchain \u2699")

    chain = BlockChain()
    print(u"\u0009\u22C5 Testing insert:")

    chain.append('2020-04-24T22:05:13Z', "some data")
    assert(chain.last.data == "some data")
    print(u"\u0009\u0009\u22C5 Insert one test passed  \U0001F44D")

    chain.append('2019-05-30T20:05:12Z', 'Moar data')
    assert(chain.last.data == 'Moar data')
    assert(chain[0].data == "some data")
    print(u"\u0009\u0009\u22C5 Insert order test passed  \U0001F44D")

    print(u"\u0009\u22C5 Testing validation:")

    chain.append('2020-05-01T05:06:14Z', 'Real data')
    assert(chain.verify() is None)
    print(u"\u0009\u0009\u22C5 Valid chain test passed  \U0001F44D")

    chain[1] = BlockChain.Block(
        '2020-02-16T10:11:36', 'Malice!', chain[0].hash)
    assert(chain[chain.verify()].data == 'Malice!')
    print(u"\u0009\u0009\u22C5 Invalid chain test passed  \U0001F44D")


if __name__ == '__main__':
    main()
    print(u"All tests passed! \U0001F60E")
