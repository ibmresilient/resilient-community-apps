from boxsdk import Client, JWTAuth
import os
import glob
import sys
import json
import logging


log = logging.getLogger(__name__)


def upload_run_file(config_file):

    # Config for Integration Box API user
    # config = {
    #
    #     "boxAppSettings": {
    #         "clientID": "81giljjokwjt5zj1skm3lkgsgrlnjlmk",
    #         "clientSecret": "zHMmbFzHzDbObU3mpH087hC95rFFZllK",
    #         "appAuth": {
    #             "publicKeyID": "3fgoc2tt",
    #             "privateKey": "-----BEGIN ENCRYPTED PRIVATE KEY-----\nMIIFDjBABgkqhkiG9w0BBQ0wMzAbBgkqhkiG9w0BBQwwDgQIGepgN2Ze6asCAggA\nMBQGCCqGSIb3DQMHBAgVLnyjsNLu6ASCBMhSvz/EMaBaxfgi9Zs6RCKyEZWAQo34\nPGcdiiu1ebD7yxAQO88tV6ZJOpKJDxQDTLVB0GsPFJsmtuViSFWPxR5bHrfvL2Q/\nCcBB1HIgMByYPRf82Pg28shushae1Cn24vGmpgaLSPJ4skcF2kdLXirpKQTdUmYj\nAE1AYVPwd9r+0rsEhxaOVUr1MGBl9Af/muT/WxhIOAX/bhkeI9l6XIgRWukwjZhR\n9/CuIoOfxpsOHDcqN3lf6pB+bmTzlzVPith+WgjFEZndz63cvifha5AoErFWVZ30\nwHlWZxYgLPoYt5cI0TmTdS95DABuxu9N8aTMNYMLNx/cR+uLDpwBEnnnjNM195Li\nqur2CcP6cPg9f5AyOyIQSGrj93juN4usMDiArvaUUteBVhepUeu3Z7OrmkSf89Y9\nkMSRt+ZqXmZMISBi3RoVD0rV4pQiH8D/NzEYH8aSrkSJwCf3fnOE39mXVg3gR9+P\n1KKuAl+oxSN916ZfOOu1Kd7LizdC7HDKDD1mnSkTr7Di+ubJ+ox4ZQcOSWUmrJu5\nMgCl1Bitgcybu5gnjO10Vo17UwE3TjzsbIyCgHw4ArMNewliVcUZRgSp2bWAvCIo\ntvZxJ/sTYiUulK5cm6VAdtYopQOd3R2N4zpV8wK6ymemx019N1OsyuqQDFmUMFlg\nAlZrI74Dkhba0JyuKe+SYQn9cqLIgYwBgUPCrQQwwoG8i/mhmBXf8T5NTyIwso03\niluof5g76f4rhJBC6/SFVR1NBS96Hsl7EjNxkR27Elx0g1tlSM0ilJhevwAQT2MM\n23Ux+CxiBOS2UYRyhx4fu91wsGLBFKdevlr43n2+PDb16baK3D8JCelxWLys/PZp\n5YzShdY35SDUM2u8/2Sc1W/RXAtUu9Az4QO2pB/xoUrFvQooM7VhlbKdWsve7u5b\nZDYhsZ/wYuAG2ixQodx6B75F+fG2TmU7LG1UWkyKtKL25FQvPGmcbvg/KExb2i5H\naPvwoDVhM6b3UNgPM9dSQKnTK8YjyVluSP86Mk2X8FYpzgHpKf+HCFEFPcLUOvE/\nUnteSGkynebHmPFvTSna95b9ts7M6o2lW8auszt/Rc7CHlD9Ex/X6ed3ViSUKDQW\nDmmJbkMBUmcVYDWG7o2GPrJIhLJ96Jcp+YqrXZ5zuxCWw2gFqnId9WZMku1AUvsz\n7ty8smSMZarXbPgPM2Bccf1Plw4q739HKS5SrenrKo5UIuZukilyXD14Bq3mfJ55\n3Z01igk/FnaZzed+h8ciKMM6hyt5H7YszgcnHnpfF24yWMAZzO7edo0yH+RwJPT4\ndLbBVq9NbZAms4p05osnohly/BIkImKyZifayNAmdAObmW50v5MzNvssjMJrfHef\n4i9QXG/ACRYtuAAFWQdus/LdtcnxMY0TVIqm9YQXGThB9If0x2IFxsu+fH384T2C\nDPRdQ1s7+7Llb5dluoXsXNd9IJHh34/hLcgK7ftHpanETwNG3Bfd0f/juPvpPTOf\nUcgG3bDpu+a2hwUgvWlrYfqCvFCZKH+/CX2iSpmafjnQwD2EDb7EUdhd9Gb3c+dv\nfBW8dVLRFWtSfUF6gyNCnBiEbsNuyDQ7CnluIJHrDH9ilZ/d7yQZOQKeA9JFTM0x\nrYA=\n-----END ENCRYPTED PRIVATE KEY-----\n",
    #             "passphrase": "6707463b2acdf329b8b17f5806726afe"
    #         }
    #     },
    #     "enterpriseID": "455328"
    # }

    # ID of the "Resilient-integration.run upload" folder
    # Can be found here: https://ibm.box.com/v/resilient-int-run-file
    folder_id = "64205016338"

    with open(config_file) as f:
        config_content = f.read()
        config_dict = json.loads(config_content)

        # Authenticate and create client
        sdk = JWTAuth.from_settings_dictionary(config_dict)
        client = Client(sdk)

        run_file_list = glob.glob(os.path.dirname(os.path.realpath(__file__)) + "/result/resilient-circuits_*.run")
        # List will only contain one item so choose the first item
        client.folder(folder_id).upload(run_file_list[0])

        file_path_list = run_file_list[0].split('/')
        log.info("{} file uploaded to Box".format(file_path_list[-1]))


if __name__ == '__main__':
    upload_run_file(sys.argv[1])
