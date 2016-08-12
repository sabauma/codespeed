# -*- coding: utf-8 -*-
####################################################
# Sample script that shows how to save result data using json #
####################################################
import urllib
import urllib2
import json
import random


# You need to enter the real URL and have the server running
CODESPEED_URL = 'http://localhost:8000/'

sample_data = []

commits = [
        "50ed6be4787890a088c8244534b3acf9a5eed885",
        "e81a2d7965adc57a9406cea39d58af196c89a1e8",
        "57a928e3afc784129c8c190ae0674bbfbad8f208",
        "dcf0429569c69956385420bffb0e2903c0b78678",
        "d880be2277052ee6a85fa8d4c6e9bbb5434eb58e",
        "52051d712c4a36d651172447b034a9509e5515b7",
        "daeff086757aa52c1c90f7108a36d3727c58ccd8",
        "8851274729a90e4051b8a1cdfb7684c21f9f5665",
        "f0d50c69a8b3720c52558d0c9ca5da1fea3825d5",
        "b379d61fa26cb4e635ab4685f48aa569a8c660d0",
        "599128ac8ffd71671e41d09177b4940d7c282880",
        "a32e4fde147143e20b59e1ab2bddfd08b9010539",
        "aeeab6391136f6642dd1b109c04736a784ae7190",
        "173465c4c5204b49d2e4b2d38134e0f9e9ef6c6f",
        "5dacb69f63f967a8c15c33e4adeb580227ddd9fc",
        "93f50721dc34db2aa625c8d5552073a043410e07",
        "44cbea8e340fb3cbd96b1761b212b60afaa4c578",
        "c817e0b86e05658c7515f7177cbea2518a11b01e",
        "635f7e51e0d36c9461c29b347e843b026c0faf4f",
        "c6d558a81ac96de47b3272add2bb0d8f2b94bab1",
        "6cb2427e313bb16d1de6f974e2c9bfb2d56d62c6",
        "dc8164ed4b20aeef32d795065a8ae4dd2e27d030",
        "d9a040348a3dc2839a0956a695c4248d9853a100",
        "dc18de85082d83300d822887b888f3019e03cfa6",
        "91255ebaf2d203c16d431f81c51df6d5f858391c",
        "37c588cb4757b3e69aeb84b798b8cdf5bc585dfd",
        "6094d1f88e3a5649102afe615ff269835fd0973a",
        "1305a0bb742feed1099714ddddc2daf8420fa5d4",
        "0b4f7113f21548024a746cfd2a85c83127e4d7d0",
        "73138dccea2a92bfa3886a9c95b00a7b9d9168b2",
        "1959906c9592e82ce293245d1874b31aea88311a",
        "0fc2534bad925f8004f86d1ae050cf513b8c4b0c",
        "1975955738824e45a478b578632abeb3a751ef74",
        "86e71070f3e129b3f7f6b3f364cab052d9f01596",
        "a3bc7724719b5fbbee7c702e309ea64fa0de4eca",
        "1400c01afc0d626801f48dbbcb663cf2387df2cd",
        "e46f6636178f8a209b70f22911b01d02556fb740",
        "400f8ba81965e687057680f499b45f9a17a82183",
        "6f33eeefd5fbfe1bad61a46b8c04f2735f7ac9d5",
        "81dd1b6c4fa6937fecc4fae550f35ae0758f7934",
        "62a005e64ff94a2b7aed6992b3e0bed507c250db",
        "88f5166eb7d4c56c5faf8cb43bf968651086c345",
        "3aed7db0abfe54a3dd9f15540f5790f7f0b0f398",
        "4c7176f228895b3c0886c2747ad8e50ea6ff04a5",
        "d62c2968f8b3ad71174f110f1345f1f0a112c6c0",
        "d2ae8a4230e75184e3163742a6f2de518d8cdb37",
        "de6e220774a2c168d9eeeb27c376a0572e99061e",
        "5a86bdfd9e4719aa47eebe1b62ed378a7c992b65",
        "2265b24d14b8a8cf3a8878284e1bffc4e5b55fc4",
        "7ae23176c901f09f9d4d9942255df8c49eae812d",
        "15da84a8b5c6f0f1eabaa09fbd09c141ae79d020",
        "9146d4fd37f98a5335083e6029df4e0dd8e4be22",
        "b5fc6c3e9e2c7e8fb4405c836baa84c80b1e48de",
        "ab8e9687630f22ea5e61ca8b785adf49358c2af4",
        "4741a97f9a1214411519d63a5670a15b3ef488fa",
        "0a95960089f5981186963fac088c2d944f40f561",
        "9071469e38ee429316c924409f0cc7f2036cc160",
        "b61bbc7011124572a3295dad11411dc3d91b6d19",
        "c3c9264415006a12eaccb963241d31da7d2f7de3",
        "acf9de7e7bc3fcd61a2bc1f7347cd05faa34c547",
        "b6ac382f36e082b046768c2f249f4b5c862301ed",
        "d96a5dbf042c5698fcd35c6885add59a331ae159",
        "7ce0af183fb11ec891f7383eaa86bdac1e3edfe7",
        "c6d8943aeddaf579d9c2a06ee7715736dd41124b",
        "06f1334ad2833bbdda39b0ea142abe9f0d1eb70b",
        "5fab14a7227d08b59907b7219d50caa73dc31ed3",
        "894d4320dc508e3585eca932edd444207f716f96",
        "26233beaf654f0e7bab8b08fbac9b5f64d48db6e",
        "a117bf19316067740acfb78fb960f381f337d092",
        "e40947cc833d8c0f60ec85fb96d1dc9c2e3d34d0",
        "2aeacc69632f3f70c015dd010d3276aa86004a4a",
        "34e778e88b752593e33a60858d5f8e8204167f24",
        "80f7aed0968765f14efad522382fc5c0ff33b562",
        "010a72ac356995ae3695f767f0096811178e5473",
        "9be15454b7c8aabadcedd108644e2463cb4d70ac",
        "28d8d2031fbd5775a7b95e8400b4fe9cf0a908e5",
        "da737e1481a9dec9b33590893a27230e645295cd",
        "cab3d05f60e05a1e27cf78c3dbcac1afd8be0112",
        "76593e9e01518341fbe6fe79047fdc70e78f2e81",
        "712f370444e0b0e537cd93898354d32166feb61b",
        "865c00c5dc3ba5558091be6dfd56405bd1f32e66",
        "7003369448841ed213b8dbd74516beb0e508f6d7",
        "bfa1aa9f672f103ee4f393a117cdb3f113410527",
        "ba093a155e8daa935a4175aabfffe27a28778dc3",
        "07a8709b0dfaa6b460d18c63480323c4a758d22c",
        "6b1b3d4d9ba30f65049c1c18270d71a20db0a38b",
        "49d0e0b2ccba046bb4aa494d8843e7ced2366d02",
        "a2ed812f37512340a03949ae9b85b2a4249e02ce",
        "409f47fa765f169000be887c15ecfdae311176ef",
        "7a0399351130a7fe8f00389b5f46dfee574e0bee",
        "318a213425659893f2f837db535895dfcc358364",
        "8fbcb081b090060d7e15beb801ee52818ad656c4",
        "8ce81004dba741fe065bdfb0749bf69e9cd31684",
        "6184ea598bc22c5fa625fd85f48e377fe63ab2bf",
        "1d212991861a23a1f31d9d3af763e1206119c65b",
        "98b5cc41ac2eab72cd312c3f5af94053c3c0d420",
        "7358263c7f99eec66a675aecafb09d59edf66a5f",
        "cdcf0c405a3f132e4140895d9d962677f49b8699",
        "ec4b55a3173bb2a495bc5698fd28d81675f9f8fe",
        "beaa34fbd24273b69de6f5420ea2ffe9662af9cd",]

for i in range(100):
    d = { "commitid": commits[i],
          "project" : "Pycket",
          "branch"  : "default",
          "executable" : "pycket-c",
          "benchmark": "CrossBenchmarks",
          "environment": "Cutter",
          "result_value": random.random() }
    sample_data.append(d)

def add(data):
    #params = urllib.urlencode(data)
    response = "None"
    try:
        f = urllib2.urlopen(
            CODESPEED_URL + 'result/add/json/', urllib.urlencode(data))
    except urllib2.HTTPError as e:
        print str(e)
        print e.read()
        return
    response = f.read()
    f.close()
    print "Server (%s) response: %s\n" % (CODESPEED_URL, response)


if __name__ == "__main__":
    data = {'json': json.dumps(sample_data)}
    add(data)
