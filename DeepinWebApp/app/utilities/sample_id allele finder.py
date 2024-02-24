####always run


import csv
# Creating lists to store data in from output.csv
poslist = []
snpidlist = []
info = []
format = []
reffreqlist = []
altfreqlist = []
homoreflist = []
homoaltlist = []
heterolist = []
#
sample_id=[]
poplist = []

# # ### CREATING 'GLOBAL' VARIABLES
wholeSIB_AC=[]
wholeSIB_AN=[]

wholeMSL_AC=[]
wholeMSL_AN=[]

wholeGBR_AC=[]
wholeGBR_AN=[]

wholeFIN_AC=[]
wholeFIN_AN=[]

wholeCHS_AC=[]
wholeCHS_AN=[]

wholePUR_AC=[]
wholePUR_AN=[]

wholeCDX_AC=[]
wholeCDX_AN=[]


wholeCLM_AC=[]
wholeCLM_AN=[]

wholeIBS_AC=[]
wholeIBS_AN=[]

wholePEL_AC=[]
wholePEL_AN=[]

wholePJL_AC=[]
wholePJL_AN=[]

wholeKHV_AC=[]
wholeKHV_AN=[]

wholeACB_AC=[]
wholeACB_AN=[]

wholeGWD_AC=[]
wholeGWD_AN=[]

wholeESN_AC=[]
wholeESN_AN=[]

wholeBEB_AC=[]
wholeBEB_AN=[]

wholeSTU_AC=[]
wholeSTU_AN=[]

wholeITU_AC=[]
wholeITU_AN=[]

wholeCEU_AC=[]
wholeCEU_AN=[]

wholeYRI_AC=[]
wholeYRI_AN=[]

wholeCHB_AC=[]
wholeCHB_AN=[]

wholeJPT_AC=[]
wholeJPT_AN=[]

wholeLWK_AC=[]
wholeLWK_AN=[]

wholeASW_AC=[]
wholeASW_AN=[]

wholeMXL_AC=[]
wholeMXL_AN=[]

wholeTSI_AC=[]
wholeTSI_AN=[]

wholeGIH_AC=[]
wholeGIH_AN=[]
#########################
wholeSIB_AF=[]
wholeACB_AF=[]
wholeASW_AF=[]
wholeESN_AF=[]
wholeGWD_AF=[]
wholeLWK_AF=[]
wholeMSL_AF=[]
wholeYRI_AF=[]
wholeCLM_AF=[]
wholeMXL_AF=[]
wholePEL_AF=[]
wholePUR_AF=[]
wholeCDX_AF=[]
wholeCHB_AF=[]
wholeCHS_AF=[]
wholeJPT_AF=[]
wholeKHV_AF=[]
wholeCEU_AF=[]
wholeFIN_AF=[]
wholeGBR_AF=[]
wholeIBS_AF=[]
wholeTSI_AF=[]
wholeBEB_AF=[]
wholeGIH_AF=[]
wholeITU_AF=[]
wholePJL_AF=[]
wholeSTU_AF=[]

#####################

wholeSIB_HOMO_REF=[]
wholeSIB_HOMO_ALT=[]
wholeSIB_HET=[]

wholeACB_HOMO_REF=[]
wholeACB_HOMO_ALT=[]
wholeACB_HET=[]

wholeASW_HOMO_REF=[]
wholeASW_HOMO_ALT=[]
wholeASW_HET=[]

wholeESN_HOMO_REF=[]
wholeESN_HOMO_ALT=[]
wholeESN_HET=[]

wholeGWD_HOMO_REF=[]
wholeGWD_HOMO_ALT=[]
wholeGWD_HET=[]

wholeLWK_HOMO_REF=[]
wholeLWK_HOMO_ALT=[]
wholeLWK_HET=[]

wholeMSL_HOMO_REF=[]
wholeMSL_HOMO_ALT=[]
wholeMSL_HET=[]

wholeYRI_HOMO_REF=[]
wholeYRI_HOMO_ALT=[]
wholeYRI_HET=[]

wholeCLM_HOMO_REF=[]
wholeCLM_HOMO_ALT=[]
wholeCLM_HET=[]

wholeMXL_HOMO_REF=[]
wholeMXL_HOMO_ALT=[]
wholeMXL_HET=[]


wholePEL_HOMO_REF=[]
wholePEL_HOMO_ALT=[]
wholePEL_HET=[]

wholePUR_HOMO_REF=[]
wholePUR_HOMO_ALT=[]
wholePUR_HET=[]


wholeCDX_HOMO_REF=[]
wholeCDX_HOMO_ALT=[]
wholeCDX_HET=[]

wholeCHB_HOMO_REF=[]
wholeCHB_HOMO_ALT=[]
wholeCHB_HET=[]

wholeCHS_HOMO_REF=[]
wholeCHS_HOMO_ALT=[]
wholeCHS_HET=[]

wholeJPT_HOMO_REF=[]
wholeJPT_HOMO_ALT=[]
wholeJPT_HET=[]

wholeKHV_HOMO_REF=[]
wholeKHV_HOMO_ALT=[]
wholeKHV_HET=[]

wholeCEU_HOMO_REF=[]
wholeCEU_HOMO_ALT=[]
wholeCEU_HET=[]


wholeFIN_HOMO_REF=[]
wholeFIN_HOMO_ALT=[]
wholeFIN_HET=[]

wholeGBR_HOMO_REF=[]
wholeGBR_HOMO_ALT=[]
wholeGBR_HET=[]


wholeIBS_HOMO_REF=[]
wholeIBS_HOMO_ALT=[]
wholeIBS_HET=[]

wholeTSI_HOMO_REF=[]
wholeTSI_HOMO_ALT=[]
wholeTSI_HET=[]

wholeBEB_HOMO_REF=[]
wholeBEB_HOMO_ALT=[]
wholeBEB_HET=[]

wholeGIH_HOMO_REF=[]
wholeGIH_HOMO_ALT=[]
wholeGIH_HET=[]

wholeITU_HOMO_REF=[]
wholeITU_HOMO_ALT=[]
wholeITU_HET=[]


wholePJL_HOMO_REF=[]
wholePJL_HOMO_ALT=[]
wholePJL_HET=[]

wholeSTU_HOMO_REF=[]
wholeSTU_HOMO_ALT=[]
wholeSTU_HET=[]





################################################################################################################################################################################################
################################################################################################################################################################################################
################################################################################################################################################################################################
with open (r'C:\Users\gaura\Downloads\id\vcf.csv', 'r') as vcffile:
    csvfile=csv.DictReader(vcffile) #creating dictreader because search for different columns using lines['column']
    for lines in csvfile:
        poslist.append(lines['POS'])
        snpidlist.append(lines['ID'])
        info.append(lines['INFO'])
        format.append(lines['FORMAT'])
vcffile.close()

with open (r'C:\Users\gaura\Downloads\group_project_data_2024\sample_pop.tsv', 'r') as samplelist:
    reader=csv.DictReader(samplelist, delimiter='\t')
    for x in reader:
        sample_id.append(x['id'])
        poplist.append(x['population'])
samplelist.close()

################################################################################################################################################################################################
################################################################################################################################################################################################
################################################################################################################################################################################################
#print(len(format))
wholeAFR_AC=[]
wholeAFR_AN=[]
wholeAFR_AF=[]
wholeAFR_HOMO_REF=[]
wholeAFR_HOMO_ALT=[]
wholeAFR_HET=[]

wholeAMR_AC=[]
wholeAMR_AN=[]
wholeAMR_AF=[]
wholeAMR_HOMO_REF=[]
wholeAMR_HOMO_ALT=[]
wholeAMR_HET=[]

wholeEAS_AC=[]
wholeEAS_AN=[]
wholeEAS_AF=[]
wholeEAS_HOMO_REF=[]
wholeEAS_HOMO_ALT=[]
wholeEAS_HET=[]

wholeEUR_AC=[]
wholeEUR_AN=[]
wholeEUR_AF=[]
wholeEUR_HOMO_REF=[]
wholeEUR_HOMO_ALT=[]
wholeEUR_HET=[]

wholeSAS_AC=[]
wholeSAS_AN=[]
wholeSAS_AF=[]
wholeSAS_HOMO_REF=[]
wholeSAS_HOMO_ALT=[]
wholeSAS_HET=[]

formatcounter=0

while formatcounter!=len(format): #while formatcounter!=len(format):
    a = list(format[formatcounter])
    removewords = ['G', 'T', '\t']
    for x in list(a):
        if x in removewords:
            a.remove(x)
    # print(a)  #['.', '/', '.', '.', '/', '.', '.', '/', '.', '.', '/', '.', '.', '/', '.', '.', '/', '.', '.
    # b=format[0] but with the genotypes joined up in better format for data analyse
    b = []
    counter = 0
    for x in a:
        b.append(''.join(a[counter:counter + 3]))
        counter = counter + 3
    # print(b[3927])  #0|0
    # print(sample_id[3927])  #NA21144
    # print(poplist[3927])  #GIH

    ################################################################################################################################################################################################
    ################################################################################################################################################################################################
    ################################################################################################################################################################################################





    SIB_AC = []
    SIB_AN = []

    GBR_AC = []
    GBR_AN = []

    FIN_AC = []
    FIN_AN = []

    CHS_AC = []
    CHS_AN = []

    PUR_AC = []
    PUR_AN = []

    CDX_AC = []
    CDX_AN = []

    CLM_AC = []
    CLM_AN = []

    IBS_AC = []
    IBS_AN = []

    PEL_AC = []
    PEL_AN = []

    PJL_AC = []
    PJL_AN = []

    KHV_AC = []
    KHV_AN = []

    ACB_AC = []
    ACB_AN = []

    GWD_AC = []
    GWD_AN = []

    ESN_AC = []
    ESN_AN = []

    BEB_AC = []
    BEB_AN = []

    MSL_AC = []
    MSL_AN = []

    STU_AC = []
    STU_AN = []

    ITU_AC = []
    ITU_AN = []

    CEU_AC = []
    CEU_AN = []

    YRI_AC = []
    YRI_AN = []

    CHB_AC = []
    CHB_AN = []

    JPT_AC = []
    JPT_AN = []

    LWK_AC = []
    LWK_AN = []

    ASW_AC = []
    ASW_AN = []

    MXL_AC = []
    MXL_AN = []

    TSI_AC = []
    TSI_AN = []

    GIH_AC = []
    GIH_AN = []

    SIB_HOMO_REF = []
    SIB_HOMO_ALT = []
    SIB_HET = []

    ACB_HOMO_REF = []
    ACB_HOMO_ALT = []
    ACB_HET = []

    ASW_HOMO_REF = []
    ASW_HOMO_ALT = []
    ASW_HET = []

    ESN_HOMO_REF = []
    ESN_HOMO_ALT = []
    ESN_HET = []

    GWD_HOMO_REF = []
    GWD_HOMO_ALT = []
    GWD_HET = []

    LWK_HOMO_REF = []
    LWK_HOMO_ALT = []
    LWK_HET = []

    MSL_HOMO_REF = []
    MSL_HOMO_ALT = []
    MSL_HET = []

    YRI_HOMO_REF = []
    YRI_HOMO_ALT = []
    YRI_HET = []

    CLM_HOMO_REF = []
    CLM_HOMO_ALT = []
    CLM_HET = []

    MXL_HOMO_REF = []
    MXL_HOMO_ALT = []
    MXL_HET = []

    PEL_HOMO_REF = []
    PEL_HOMO_ALT = []
    PEL_HET = []

    PUR_HOMO_REF = []
    PUR_HOMO_ALT = []
    PUR_HET = []

    CDX_HOMO_REF = []
    CDX_HOMO_ALT = []
    CDX_HET = []

    CHB_HOMO_REF = []
    CHB_HOMO_ALT = []
    CHB_HET = []

    CHS_HOMO_REF = []
    CHS_HOMO_ALT = []
    CHS_HET = []

    JPT_HOMO_REF = []
    JPT_HOMO_ALT = []
    JPT_HET = []

    KHV_HOMO_REF = []
    KHV_HOMO_ALT = []
    KHV_HET = []

    CEU_HOMO_REF = []
    CEU_HOMO_ALT = []
    CEU_HET = []

    FIN_HOMO_REF = []
    FIN_HOMO_ALT = []
    FIN_HET = []

    GBR_HOMO_REF = []
    GBR_HOMO_ALT = []
    GBR_HET = []

    IBS_HOMO_REF = []
    IBS_HOMO_ALT = []
    IBS_HET = []

    TSI_HOMO_REF = []
    TSI_HOMO_ALT = []
    TSI_HET = []

    BEB_HOMO_REF = []
    BEB_HOMO_ALT = []
    BEB_HET = []

    GIH_HOMO_REF = []
    GIH_HOMO_ALT = []
    GIH_HET = []

    ITU_HOMO_REF = []
    ITU_HOMO_ALT = []
    ITU_HET = []

    PJL_HOMO_REF = []
    PJL_HOMO_ALT = []
    PJL_HET = []

    STU_HOMO_REF = []
    STU_HOMO_ALT = []
    STU_HET = []


    AFR_AC=[]
    AFR_AN=[]
    AFR_HOMO_REF=[]
    AFR_HOMO_ALT=[]
    AFR_HET=[]

    AMR_AC=[]
    AMR_AN=[]
    AMR_HOMO_REF=[]
    AMR_HOMO_ALT=[]
    AMR_HET=[]

    EAS_AC=[]
    EAS_AN=[]
    EAS_HOMO_REF=[]
    EAS_HOMO_ALT=[]
    EAS_HET=[]

    EUR_AC=[]
    EUR_AN=[]
    EUR_HOMO_REF=[]
    EUR_HOMO_ALT=[]
    EUR_HET=[]

    SAS_AC=[]
    SAS_AN=[]
    EUR_HOMO_REF=[]
    EUR_HOMO_ALT=[]
    EUR_HET=[]



    counter = 0
    # b is format[0]
    for x in b:
        if x == '0/0':
            if poplist[counter] == 'SIB':
                SIB_AN.append('2')
        if x == '0|0':
            if poplist[counter] == 'SIB':
                SIB_AN.append('2')

            if poplist[counter] == 'ACB':
                ACB_AN.append('2')
                AFR_AN.append('2')

            if poplist[counter] == 'ASW':
                ASW_AN.append('2')
                AFR_AN.append('2')
            if poplist[counter] == 'ESN':
                ESN_AN.append('2')
                AFR_AN.append('2')

            if poplist[counter] == 'GWD':
                GWD_AN.append('2')
                AFR_AN.append('2')

            if poplist[counter] == 'LWK':
                LWK_AN.append('2')
                AFR_AN.append('2')

            if poplist[counter] == 'MSL':
                MSL_AN.append('2')
                AFR_AN.append('2')

            if poplist[counter] == 'YRI':
                YRI_AN.append('2')
                AFR_AN.append('2')

            if poplist[counter] == 'CLM':
                CLM_AN.append('2')
                AMR_AN.append('2')
            if poplist[counter] == 'MXL':
                MXL_AN.append('2')
                AMR_AN.append('2')

            if poplist[counter] == 'PEL':
                PEL_AN.append('2')
                AMR_AN.append('2')

            if poplist[counter] == 'PUR':
                PUR_AN.append('2')
                AMR_AN.append('2')

            if poplist[counter] == 'CDX':
                CDX_AN.append('2')
                EAS_AN.append('2')
            if poplist[counter] == 'CHB':
                CHB_AN.append('2')
                EAS_AN.append('2')

            if poplist[counter] == 'CHS':
                CHS_AN.append('2')
                EAS_AN.append('2')

            if poplist[counter] == 'JPT':
                JPT_AN.append('2')
                EAS_AN.append('2')

            if poplist[counter] == 'KHV':
                KHV_AN.append('2')
                EAS_AN.append('2')

            if poplist[counter] == 'CEU':
                CEU_AN.append('2')
                EUR_AN.append('2')

            if poplist[counter] == 'FIN':
                FIN_AN.append('2')
                EUR_AN.append('2')
            if poplist[counter] == 'GBR':
                GBR_AN.append('2')
                EUR_AN.append('2')

            if poplist[counter] == 'IBS':
                IBS_AN.append('2')
                EUR_AN.append('2')
            if poplist[counter] == 'TSI':
                TSI_AN.append('2')
                EUR_AN.append('2')

            if poplist[counter] == 'BEB':
                BEB_AN.append('2')
                SAS_AN.append('2')
            if poplist[counter] == 'GIH':
                GIH_AN.append('2')
                SAS_AN.append('2')

            if poplist[counter] == 'ITU':
                ITU_AN.append('2')
                SAS_AN.append('2')

            if poplist[counter] == 'PJL':
                PJL_AN.append('2')
                SAS_AN.append('2')

            if poplist[counter] == 'STU':
                STU_AN.append('2')
                SAS_AN.append('2')

        if x == '0|1':
            if poplist[counter] == 'SIB':
                SIB_AN.append('2')
                SIB_AC.append('1')

            if poplist[counter] == 'ACB':
                ACB_AN.append('2')
                ACB_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')
            if poplist[counter] == 'ASW':
                ASW_AN.append('2')
                ASW_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')

            if poplist[counter] == 'ESN':
                ESN_AN.append('2')
                ESN_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')

            if poplist[counter] == 'GWD':
                GWD_AN.append('2')
                GWD_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')

            if poplist[counter] == 'LWK':
                LWK_AN.append('2')
                LWK_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')

            if poplist[counter] == 'MSL':
                MSL_AN.append('2')
                MSL_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')
            if poplist[counter] == 'YRI':
                YRI_AN.append('2')
                YRI_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')

            if poplist[counter] == 'CLM':
                CLM_AN.append('2')
                CLM_AC.append('1')
                AMR_AN.append('2')
                AMR_AC.append('1')

            if poplist[counter] == 'MXL':
                MXL_AN.append('2')
                MXL_AC.append('1')
                AMR_AN.append('2')
                AMR_AC.append('1')

            if poplist[counter] == 'PEL':
                PEL_AN.append('2')
                PEL_AC.append('1')
                AMR_AN.append('2')
                AMR_AC.append('1')

            if poplist[counter] == 'PUR':
                PUR_AN.append('2')
                PUR_AC.append('1')
                AMR_AN.append('2')
                AMR_AC.append('1')

            if poplist[counter] == 'CDX':
                CDX_AN.append('2')
                CDX_AC.append('1')
                EAS_AN.append('2')
                EAS_AC.append('1')

            if poplist[counter] == 'CHB':
                CHB_AN.append('2')
                CHB_AC.append('1')
                EAS_AN.append('2')
                EAS_AC.append('1')

            if poplist[counter] == 'CHS':
                CHS_AN.append('2')
                CHS_AC.append('1')
                EAS_AN.append('2')
                EAS_AC.append('1')

            if poplist[counter] == 'JPT':
                JPT_AN.append('2')
                JPT_AC.append('1')
                EAS_AN.append('2')
                EAS_AC.append('1')

            if poplist[counter] == 'KHV':
                KHV_AN.append('2')
                KHV_AC.append('1')
                EAS_AN.append('2')
                EAS_AC.append('1')

            if poplist[counter] == 'CEU':
                CEU_AN.append('2')
                CEU_AC.append('1')
                EUR_AN.append('2')
                EUR_AC.append('1')

            if poplist[counter] == 'FIN':
                FIN_AN.append('2')
                FIN_AC.append('1')
                EUR_AN.append('2')
                EUR_AC.append('1')

            if poplist[counter] == 'GBR':
                GBR_AN.append('2')
                GBR_AC.append('1')
                EUR_AN.append('2')
                EUR_AC.append('1')

            if poplist[counter] == 'IBS':
                IBS_AN.append('2')
                IBS_AC.append('1')
                EUR_AN.append('2')
                EUR_AC.append('1')

            if poplist[counter] == 'TSI':
                TSI_AN.append('2')
                TSI_AC.append('1')
                EUR_AN.append('2')
                EUR_AC.append('1')

            if poplist[counter] == 'BEB':
                BEB_AN.append('2')
                BEB_AC.append('1')
                SAS_AN.append('2')
                SAS_AC.append('1')

            if poplist[counter] == 'GIH':
                GIH_AN.append('2')
                GIH_AC.append('1')
                SAS_AN.append('2')
                SAS_AC.append('1')

            if poplist[counter] == 'ITU':
                ITU_AN.append('2')
                ITU_AC.append('1')
                SAS_AN.append('2')
                SAS_AC.append('1')

            if poplist[counter] == 'PJL':
                PJL_AN.append('2')
                PJL_AC.append('1')
                SAS_AN.append('2')
                SAS_AC.append('1')

            if poplist[counter] == 'STU':
                STU_AN.append('2')
                STU_AC.append('1')
                SAS_AN.append('2')
                SAS_AC.append('1')

        if x == '1|0':
            if poplist[counter] == 'SIB':
                SIB_AN.append('2')
                SIB_AC.append('1')

            if poplist[counter] == 'ACB':
                ACB_AN.append('2')
                ACB_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')

            if poplist[counter] == 'ASW':
                ASW_AN.append('2')
                ASW_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')

            if poplist[counter] == 'ESN':
                ESN_AN.append('2')
                ESN_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')

            if poplist[counter] == 'GWD':
                GWD_AN.append('2')
                GWD_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')

            if poplist[counter] == 'LWK':
                LWK_AN.append('2')
                LWK_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')

            if poplist[counter] == 'MSL':
                MSL_AN.append('2')
                MSL_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')

            if poplist[counter] == 'YRI':
                YRI_AN.append('2')
                YRI_AC.append('1')
                AFR_AN.append('2')
                AFR_AC.append('1')

            if poplist[counter] == 'CLM':
                CLM_AN.append('2')
                CLM_AC.append('1')
                AMR_AN.append('2')
                AMR_AC.append('1')

            if poplist[counter] == 'MXL':
                MXL_AN.append('2')
                MXL_AC.append('1')
                AMR_AN.append('2')
                AMR_AC.append('1')

            if poplist[counter] == 'PEL':
                PEL_AN.append('2')
                PEL_AC.append('1')
                AMR_AN.append('2')
                AMR_AC.append('1')

            if poplist[counter] == 'PUR':
                PUR_AN.append('2')
                PUR_AC.append('1')
                AMR_AN.append('2')
                AMR_AC.append('1')

            if poplist[counter] == 'CDX':
                CDX_AN.append('2')
                CDX_AC.append('1')
                EAS_AN.append('2')
                EAS_AC.append('1')

            if poplist[counter] == 'CHB':
                CHB_AN.append('2')
                CHB_AC.append('1')
                EAS_AN.append('2')
                EAS_AC.append('1')

            if poplist[counter] == 'CHS':
                CHS_AN.append('2')
                CHS_AC.append('1')
                EAS_AN.append('2')
                EAS_AC.append('1')

            if poplist[counter] == 'JPT':
                JPT_AN.append('2')
                JPT_AC.append('1')
                EAS_AN.append('2')
                EAS_AC.append('1')

            if poplist[counter] == 'KHV':
                KHV_AN.append('2')
                KHV_AC.append('1')
                EAS_AN.append('2')
                EAS_AC.append('1')

            if poplist[counter] == 'CEU':
                CEU_AN.append('2')
                CEU_AC.append('1')
                EUR_AN.append('2')
                EUR_AC.append('1')

            if poplist[counter] == 'FIN':
                FIN_AN.append('2')
                FIN_AC.append('1')
                EUR_AN.append('2')
                EUR_AC.append('1')

            if poplist[counter] == 'GBR':
                GBR_AN.append('2')
                GBR_AC.append('1')
                EUR_AN.append('2')
                EUR_AC.append('1')

            if poplist[counter] == 'IBS':
                IBS_AN.append('2')
                IBS_AC.append('1')
                EUR_AN.append('2')
                EUR_AC.append('1')

            if poplist[counter] == 'TSI':
                TSI_AN.append('2')
                TSI_AC.append('1')
                EUR_AN.append('2')
                EUR_AC.append('1')

            if poplist[counter] == 'BEB':
                BEB_AN.append('2')
                BEB_AC.append('1')
                SAS_AN.append('2')
                SAS_AC.append('1')

            if poplist[counter] == 'GIH':
                GIH_AN.append('2')
                GIH_AC.append('1')
                SAS_AN.append('2')
                SAS_AC.append('1')

            if poplist[counter] == 'ITU':
                ITU_AN.append('2')
                ITU_AC.append('1')
                SAS_AN.append('2')
                SAS_AC.append('1')

            if poplist[counter] == 'PJL':
                PJL_AN.append('2')
                PJL_AC.append('1')
                SAS_AN.append('2')
                SAS_AC.append('1')

            if poplist[counter] == 'STU':
                STU_AN.append('2')
                STU_AC.append('1')
                SAS_AN.append('2')
                SAS_AC.append('1')

        if x == '1|1':
            if poplist[counter] == 'SIB':
                SIB_AN.append('2')
                SIB_AC.append('2')


            if poplist[counter] == 'ACB':
                ACB_AN.append('2')
                ACB_AC.append('2')
                AFR_AN.append('2')
                AFR_AC.append('2')

            if poplist[counter] == 'ASW':
                ASW_AN.append('2')
                ASW_AC.append('2')
                AFR_AN.append('2')
                AFR_AC.append('2')

            if poplist[counter] == 'ESN':
                ESN_AN.append('2')
                ESN_AC.append('2')
                AFR_AN.append('2')
                AFR_AC.append('2')

            if poplist[counter] == 'GWD':
                GWD_AN.append('2')
                GWD_AC.append('2')
                AFR_AN.append('2')
                AFR_AC.append('2')

            if poplist[counter] == 'LWK':
                LWK_AN.append('2')
                LWK_AC.append('2')
                AFR_AN.append('2')
                AFR_AC.append('2')

            if poplist[counter] == 'MSL':
                MSL_AN.append('2')
                MSL_AC.append('2')
                AFR_AN.append('2')
                AFR_AC.append('2')

            if poplist[counter] == 'YRI':
                YRI_AN.append('2')
                YRI_AC.append('2')
                AFR_AN.append('2')
                AFR_AC.append('2')

            if poplist[counter] == 'CLM':
                CLM_AN.append('2')
                CLM_AC.append('2')
                AMR_AN.append('2')
                AMR_AC.append('2')

            if poplist[counter] == 'MXL':
                MXL_AN.append('2')
                MXL_AC.append('2')
                AMR_AN.append('2')
                AMR_AC.append('2')

            if poplist[counter] == 'PEL':
                PEL_AN.append('2')
                PEL_AC.append('2')
                AMR_AN.append('2')
                AMR_AC.append('2')

            if poplist[counter] == 'PUR':
                PUR_AN.append('2')
                PUR_AC.append('2')
                AMR_AN.append('2')
                AMR_AC.append('2')

            if poplist[counter] == 'CDX':
                CDX_AN.append('2')
                CDX_AC.append('2')
                EAS_AN.append('2')
                EAS_AC.append('2')

            if poplist[counter] == 'CHB':
                CHB_AN.append('2')
                CHB_AC.append('2')
                EAS_AN.append('2')
                EAS_AC.append('2')

            if poplist[counter] == 'CHS':
                CHS_AN.append('2')
                CHS_AC.append('2')
                EAS_AN.append('2')
                EAS_AC.append('2')

            if poplist[counter] == 'JPT':
                JPT_AN.append('2')
                JPT_AC.append('2')
                EAS_AN.append('2')
                EAS_AC.append('2')

            if poplist[counter] == 'KHV':
                KHV_AN.append('2')
                KHV_AC.append('2')
                EAS_AN.append('2')
                EAS_AC.append('2')

            if poplist[counter] == 'CEU':
                CEU_AN.append('2')
                CEU_AC.append('2')
                EUR_AN.append('2')
                EUR_AC.append('2')

            if poplist[counter] == 'FIN':
                FIN_AN.append('2')
                FIN_AC.append('2')
                EUR_AN.append('2')
                EUR_AC.append('2')

            if poplist[counter] == 'GBR':
                GBR_AN.append('2')
                GBR_AC.append('2')
                EUR_AN.append('2')
                EUR_AC.append('2')

            if poplist[counter] == 'IBS':
                IBS_AN.append('2')
                IBS_AC.append('2')
                EUR_AN.append('2')
                EUR_AC.append('2')

            if poplist[counter] == 'TSI':
                TSI_AN.append('2')
                TSI_AC.append('2')
                EUR_AN.append('2')
                EUR_AC.append('2')

            if poplist[counter] == 'BEB':
                BEB_AN.append('2')
                BEB_AC.append('2')
                SAS_AN.append('2')
                SAS_AC.append('2')

            if poplist[counter] == 'GIH':
                GIH_AN.append('2')
                GIH_AC.append('2')
                SAS_AN.append('2')
                SAS_AC.append('2')

            if poplist[counter] == 'ITU':
                ITU_AN.append('2')
                ITU_AC.append('2')
                SAS_AN.append('2')
                SAS_AC.append('2')

            if poplist[counter] == 'PJL':
                PJL_AN.append('2')
                PJL_AC.append('2')
                SAS_AN.append('2')
                SAS_AC.append('2')

            if poplist[counter] == 'STU':
                STU_AN.append('2')
                STU_AC.append('2')
                SAS_AN.append('2')
                SAS_AC.append('2')

        if x == './.':
            if poplist[counter] == 'SIB':
                SIB_AN.append('0')
            if poplist[counter] == 'ACB':
                ACB_AN.append('0')
                AFR_AN.append('0')
            if poplist[counter] == 'ASW':
                ASW_AN.append('0')
                AFR_AN.append('0')

            if poplist[counter] == 'ESN':
                ESN_AN.append('0')
                AFR_AN.append('0')

            if poplist[counter] == 'GWD':
                GWD_AN.append('0')
                AFR_AN.append('0')

            if poplist[counter] == 'LWK':
                LWK_AN.append('0')
                AFR_AN.append('0')

            if poplist[counter] == 'MSL':
                MSL_AN.append('0')
                AFR_AN.append('0')

            if poplist[counter] == 'YRI':
                YRI_AN.append('0')
                AFR_AN.append('0')

            if poplist[counter] == 'CLM':
                CLM_AN.append('0')
                AMR_AN.append('0')

            if poplist[counter] == 'MXL':
                MXL_AN.append('0')
                AMR_AN.append('0')

            if poplist[counter] == 'PEL':
                PEL_AN.append('0')
                AMR_AN.append('0')

            if poplist[counter] == 'PUR':
                PUR_AN.append('0')
                AMR_AN.append('0')

            if poplist[counter] == 'CDX':
                CDX_AN.append('0')
                EAS_AN.append('0')

            if poplist[counter] == 'CHB':
                CHB_AN.append('0')
                EAS_AN.append('0')

            if poplist[counter] == 'CHS':
                CHS_AN.append('0')
                EAS_AN.append('0')

            if poplist[counter] == 'JPT':
                JPT_AN.append('0')
                EAS_AN.append('0')

            if poplist[counter] == 'KHV':
                KHV_AN.append('0')
                EAS_AN.append('0')

            if poplist[counter] == 'CEU':
                CEU_AN.append('0')
                EUR_AN.append('0')

            if poplist[counter] == 'FIN':
                FIN_AN.append('0')
                EUR_AN.append('0')

            if poplist[counter] == 'GBR':
                GBR_AN.append('0')
                EUR_AN.append('0')

            if poplist[counter] == 'IBS':
                IBS_AN.append('0')
                EUR_AN.append('0')

            if poplist[counter] == 'TSI':
                TSI_AN.append('0')
                EUR_AN.append('0')

            if poplist[counter] == 'BEB':
                BEB_AN.append('0')
                SAS_AN.append('0')

            if poplist[counter] == 'GIH':
                GIH_AN.append('0')
                SAS_AN.append('0')

            if poplist[counter] == 'ITU':
                ITU_AN.append('0')
                SAS_AN.append('0')

            if poplist[counter] == 'PJL':
                PJL_AN.append('0')
                SAS_AN.append('0')

            if poplist[counter] == 'STU':
                STU_AN.append('0')
                SAS_AN.append('0')

        counter = counter + 1

    # if SIB_AN.count('0')>0 this means that there is ./. instead of 0|0 or 0|1 or 1|0 or 1|1
    if AFR_AN.count('0') > 0:
        wholeAFR_AN.append(0)
        wholeAFR_AC.append(0)
    elif AFR_AN.count('0')==0:
        test=AFR_AN.count('2') * 2
        wholeAFR_AN.append(test)
        test=AFR_AC.count('1')
        test1=AFR_AC.count('2')*2
        test3=test+test1
        wholeAFR_AC.append(test3)

    if AMR_AN.count('0') > 0:
        wholeAMR_AN.append(0)
        wholeAMR_AC.append(0)
    elif AMR_AN.count('0') == 0:
        test = AMR_AN.count('2') * 2
        wholeAMR_AN.append(test)
        test = AMR_AC.count('1')
        test1 = AMR_AC.count('2') * 2
        test3 = test + test1
        wholeAMR_AC.append(test3)

    if EAS_AN.count('0') > 0:
        wholeEAS_AN.append(0)
        wholeEAS_AC.append(0)
    elif EAS_AN.count('0') == 0:
        test = EAS_AN.count('2') * 2
        wholeEAS_AN.append(test)
        test = EAS_AC.count('1')
        test1 = EAS_AC.count('2') * 2
        test3 = test + test1
        wholeEAS_AC.append(test3)

    if EUR_AN.count('0') > 0:
        wholeEUR_AN.append(0)
        wholeEUR_AC.append(0)
    elif EUR_AN.count('0') == 0:
        test = EUR_AN.count('2') * 2
        wholeEUR_AN.append(test)
        test = EUR_AC.count('1')
        test1 = EUR_AC.count('2') * 2
        test3 = test + test1
        wholeEUR_AC.append(test3)

    if SAS_AN.count('0') > 0:
        wholeSAS_AN.append(0)
        wholeSAS_AC.append(0)
    elif SAS_AN.count('0') == 0:
        test = SAS_AN.count('2') * 2
        wholeSAS_AN.append(test)
        test = SAS_AC.count('1')
        test1 = SAS_AC.count('2') * 2
        test3 = test + test1
        wholeSAS_AC.append(test3)



    if SIB_AN.count('0') > 0:
        wholeSIB_AN.append(0)
        wholeSIB_AC.append(0)
    elif SIB_AN.count('0') == 0:
        test = SIB_AN.count('2') * 2
        wholeSIB_AN.append(test)
        test = SIB_AC.count('1')
        test1 = SIB_AC.count('2') * 2
        test3 = test + test1
        wholeSIB_AC.append(test3)



    if MSL_AN.count('0') > 0:
        wholeMSL_AN.append(0)
        wholeMSL_AC.append(0)
    elif MSL_AN.count('0') == 0:
        test = MSL_AN.count('2') * 2
        wholeMSL_AN.append(test)
        test = MSL_AC.count('1')
        test1 = MSL_AC.count('2') * 2
        test3 = test + test1
        wholeMSL_AC.append(test3)


    if GBR_AN.count('0') > 0:
        wholeGBR_AN.append(0)
        wholeGBR_AC.append(0)
    elif GBR_AN.count('0') == 0:
        test = GBR_AN.count('2') * 2
        wholeGBR_AN.append(test)
        test = GBR_AC.count('1')
        test1 = GBR_AC.count('2') * 2
        test3 = test + test1
        wholeGBR_AC.append(test3)


    if FIN_AN.count('0') > 0:
        wholeFIN_AN.append(0)
        wholeFIN_AC.append(0)
    elif FIN_AN.count('0') == 0:
        test = FIN_AN.count('2') * 2
        wholeFIN_AN.append(test)
        test = FIN_AC.count('1')
        test1 = FIN_AC.count('2') * 2
        test3 = test + test1
        wholeFIN_AC.append(test3)


    if CHS_AN.count('0') > 0:
        wholeCHS_AN.append(0)
        wholeCHS_AC.append(0)
    elif CHS_AN.count('0') == 0:
        test = CHS_AN.count('2') * 2
        wholeCHS_AN.append(test)
        test = CHS_AC.count('1')
        test1 = CHS_AC.count('2') * 2
        test3 = test + test1
        wholeCHS_AC.append(test3)


    if PUR_AN.count('0') > 0:
        wholePUR_AN.append(0)
        wholePUR_AC.append(0)
    elif PUR_AN.count('0') == 0:
        test = PUR_AN.count('2') * 2
        wholePUR_AN.append(test)
        test = PUR_AC.count('1')
        test1 = PUR_AC.count('2') * 2
        test3 = test + test1
        wholePUR_AC.append(test3)


    if CDX_AN.count('0') > 0:
        wholeCDX_AN.append(0)
        wholeCDX_AC.append(0)
    elif CDX_AN.count('0') == 0:
        test = CDX_AN.count('2') * 2
        wholeCDX_AN.append(test)
        test = CDX_AC.count('1')
        test1 = CDX_AC.count('2') * 2
        test3 = test + test1
        wholeCDX_AC.append(test3)


    if CLM_AN.count('0') > 0:
        wholeCLM_AN.append(0)
        wholeCLM_AC.append(0)
    elif CLM_AN.count('0') == 0:
        test = CLM_AN.count('2') * 2
        wholeCLM_AN.append(test)
        test = CLM_AC.count('1')
        test1 = CLM_AC.count('2') * 2
        test3 = test + test1
        wholeCLM_AC.append(test3)


    if IBS_AN.count('0') > 0:
        wholeIBS_AN.append(0)
        wholeIBS_AC.append(0)
    elif IBS_AN.count('0') == 0:
        test = IBS_AN.count('2') * 2
        wholeIBS_AN.append(test)
        test = IBS_AC.count('1')
        test1 = IBS_AC.count('2') * 2
        test3 = test + test1
        wholeIBS_AC.append(test3)


    if PEL_AN.count('0') > 0:
        wholePEL_AN.append(0)
        wholePEL_AC.append(0)
    elif PEL_AN.count('0') == 0:
        test = PEL_AN.count('2') * 2
        wholePEL_AN.append(test)
        test = PEL_AC.count('1')
        test1 = PEL_AC.count('2') * 2
        test3 = test + test1
        wholePEL_AC.append(test3)


    if PJL_AN.count('0') > 0:
        wholePJL_AN.append(0)
        wholePJL_AC.append(0)
    elif PJL_AN.count('0') == 0:
        test = PJL_AN.count('2') * 2
        wholePJL_AN.append(test)
        test = PJL_AC.count('1')
        test1 = PJL_AC.count('2') * 2
        test3 = test + test1
        wholePJL_AC.append(test3)


    if KHV_AN.count('0') > 0:
        wholeKHV_AN.append(0)
        wholeKHV_AC.append(0)
    elif KHV_AN.count('0') == 0:
        test = KHV_AN.count('2') * 2
        wholeKHV_AN.append(test)
        test = KHV_AC.count('1')
        test1 = KHV_AC.count('2') * 2
        test3 = test + test1
        wholeKHV_AC.append(test3)


    if ACB_AN.count('0') > 0:
        wholeACB_AN.append(0)
        wholeACB_AC.append(0)
    elif ACB_AN.count('0') == 0:
        test = ACB_AN.count('2') * 2
        wholeACB_AN.append(test)
        test = ACB_AC.count('1')
        test1 = ACB_AC.count('2') * 2
        test3 = test + test1
        wholeACB_AC.append(test3)


    if GWD_AN.count('0') > 0:
        wholeGWD_AN.append(0)
        wholeGWD_AC.append(0)
    elif GWD_AN.count('0') == 0:
        test = GWD_AN.count('2') * 2
        wholeGWD_AN.append(test)
        test = GWD_AC.count('1')
        test1 = GWD_AC.count('2') * 2
        test3 = test + test1
        wholeGWD_AC.append(test3)


    if ESN_AN.count('0') > 0:
        wholeESN_AN.append(0)
        wholeESN_AC.append(0)
    elif ESN_AN.count('0') == 0:
        test = ESN_AN.count('2') * 2
        wholeESN_AN.append(test)
        test = ESN_AC.count('1')
        test1 = ESN_AC.count('2') * 2
        test3 = test + test1
        wholeESN_AC.append(test3)


    if BEB_AN.count('0') > 0:
        wholeBEB_AN.append(0)
        wholeBEB_AC.append(0)
    elif BEB_AN.count('0') == 0:
        test = BEB_AN.count('2') * 2
        wholeBEB_AN.append(test)
        test = BEB_AC.count('1')
        test1 = BEB_AC.count('2') * 2
        test3 = test + test1
        wholeBEB_AC.append(test3)


    if STU_AN.count('0') > 0:
        wholeSTU_AN.append(0)
        wholeSTU_AC.append(0)
    elif STU_AN.count('0') == 0:
        test = STU_AN.count('2') * 2
        wholeSTU_AN.append(test)
        test = STU_AC.count('1')
        test1 = STU_AC.count('2') * 2
        test3 = test + test1
        wholeSTU_AC.append(test3)


    if ITU_AN.count('0') > 0:
        wholeITU_AN.append(0)
        wholeITU_AC.append(0)
    elif ITU_AN.count('0') == 0:
        test = ITU_AN.count('2') * 2
        wholeITU_AN.append(test)
        test = ITU_AC.count('1')
        test1 = ITU_AC.count('2') * 2
        test3 = test + test1
        wholeITU_AC.append(test3)


    if CEU_AN.count('0') > 0:
        wholeCEU_AN.append(0)
        wholeCEU_AC.append(0)
    elif CEU_AN.count('0') == 0:
        test = CEU_AN.count('2') * 2
        wholeCEU_AN.append(test)
        test = CEU_AC.count('1')
        test1 = CEU_AC.count('2') * 2
        test3 = test + test1
        wholeCEU_AC.append(test3)


    if YRI_AN.count('0') > 0:
        wholeYRI_AN.append(0)
        wholeYRI_AC.append(0)
    elif YRI_AN.count('0') == 0:
        test = YRI_AN.count('2') * 2
        wholeYRI_AN.append(test)
        test = YRI_AC.count('1')
        test1 = YRI_AC.count('2') * 2
        test3 = test + test1
        wholeYRI_AC.append(test3)


    if CHB_AN.count('0') > 0:
        wholeCHB_AN.append(0)
        wholeCHB_AC.append(0)
    elif CHB_AN.count('0') == 0:
        test = CHB_AN.count('2') * 2
        wholeCHB_AN.append(test)
        test = CHB_AC.count('1')
        test1 = CHB_AC.count('2') * 2
        test3 = test + test1
        wholeCHB_AC.append(test3)


    if JPT_AN.count('0') > 0:
        wholeJPT_AN.append(0)
        wholeJPT_AC.append(0)
    elif JPT_AN.count('0') == 0:
        test = JPT_AN.count('2') * 2
        wholeJPT_AN.append(test)
        test = JPT_AC.count('1')
        test1 = JPT_AC.count('2') * 2
        test3 = test + test1
        wholeJPT_AC.append(test3)


    if LWK_AN.count('0') > 0:
        wholeLWK_AN.append(0)
        wholeLWK_AC.append(0)
    elif LWK_AN.count('0') == 0:
        test = LWK_AN.count('2') * 2
        wholeLWK_AN.append(test)
        test = LWK_AC.count('1')
        test1 = LWK_AC.count('2') * 2
        test3 = test + test1
        wholeLWK_AC.append(test3)

    if ASW_AN.count('0') > 0:
        wholeASW_AN.append(0)
        wholeASW_AC.append(0)
    elif ASW_AN.count('0') == 0:
        test = ASW_AN.count('2') * 2
        wholeASW_AN.append(test)
        test = ASW_AC.count('1')
        test1 = ASW_AC.count('2') * 2
        test3 = test + test1
        wholeASW_AC.append(test3)

    if MXL_AN.count('0') > 0:
        wholeMXL_AN.append(0)
        wholeMXL_AC.append(0)
    elif MXL_AN.count('0') == 0:
        test = MXL_AN.count('2') * 2
        wholeMXL_AN.append(test)
        test = MXL_AC.count('1')
        test1 = MXL_AC.count('2') * 2
        test3 = test + test1
        wholeMXL_AC.append(test3)


    if TSI_AN.count('0') > 0:
        wholeTSI_AN.append(0)
        wholeTSI_AC.append(0)
    elif TSI_AN.count('0') == 0:
        test = TSI_AN.count('2') * 2
        wholeTSI_AN.append(test)
        test = TSI_AC.count('1')
        test1 = TSI_AC.count('2') * 2
        test3 = test + test1
        wholeTSI_AC.append(test3)

    if GIH_AN.count('0') > 0:
        wholeGIH_AN.append(0)
        wholeGIH_AC.append(0)
    elif GIH_AN.count('0') == 0:
        test = GIH_AN.count('2') * 2
        wholeGIH_AN.append(test)
        test = GIH_AC.count('1')
        test1 = GIH_AC.count('2') * 2
        test3 = test + test1
        wholeGIH_AC.append(test3)


    ##############################################################################################################################################
    ###########################        CALCULATING GENOTYPE FREQEUNCIES FOR EACH POPULATION       ################################################
    ##############################################################################################################################################

    if wholeAFR_AN[-1] == 0:
        wholeAFR_HOMO_ALT.append('NaN')
        wholeAFR_HOMO_REF.append('NaN')
        wholeAFR_HET.append('NaN')
        wholeAFR_AF.append('NaN')
    elif wholeAFR_AN[-1] != 0:
        test = (wholeAFR_AC[-1]) / (wholeAFR_AN[-1])
        wholeAFR_AF.append(test)
        wholeAFR_HOMO_ALT.append(test * test)
        test1= 1 - test
        wholeAFR_HOMO_REF.append(test1 * test1)
        wholeAFR_HET.append(2*test*test1)

    if wholeAMR_AN[-1] == 0:
        wholeAMR_HOMO_ALT.append('NaN')
        wholeAMR_HOMO_REF.append('NaN')
        wholeAMR_HET.append('NaN')
        wholeAMR_AF.append('NaN')
    elif wholeAMR_AN[-1] != 0:
        test = (wholeAMR_AC[-1]) / (wholeAMR_AN[-1])
        wholeAMR_AF.append(test)
        wholeAMR_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeAMR_HOMO_REF.append(test1 * test1)
        wholeAMR_HET.append(2 * test * test1)

    if wholeEAS_AN[-1] == 0:
        wholeEAS_HOMO_ALT.append('NaN')
        wholeEAS_HOMO_REF.append('NaN')
        wholeEAS_HET.append('NaN')
        wholeEAS_AF.append('NaN')
    elif wholeEAS_AN[-1] != 0:
        test = (wholeEAS_AC[-1]) / (wholeEAS_AN[-1])
        wholeEAS_AF.append(test)
        wholeEAS_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeEAS_HOMO_REF.append(test1 * test1)
        wholeEAS_HET.append(2 * test * test1)

    if wholeEUR_AN[-1] == 0:
        wholeEUR_HOMO_ALT.append('NaN')
        wholeEUR_HOMO_REF.append('NaN')
        wholeEUR_HET.append('NaN')
        wholeEUR_AF.append('NaN')
    elif wholeEUR_AN[-1] != 0:
        test = (wholeEUR_AC[-1]) / (wholeEUR_AN[-1])
        wholeEUR_AF.append(test)
        wholeEUR_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeEUR_HOMO_REF.append(test1 * test1)
        wholeEUR_HET.append(2 * test * test1)

    if wholeSAS_AN[-1] == 0:
        wholeSAS_HOMO_ALT.append('NaN')
        wholeSAS_HOMO_REF.append('NaN')
        wholeSAS_HET.append('NaN')
        wholeSAS_AF.append('NaN')
    elif wholeSAS_AN[-1] != 0:
        test = (wholeSAS_AC[-1]) / (wholeSAS_AN[-1])
        wholeSAS_AF.append(test)
        wholeSAS_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeSAS_HOMO_REF.append(test1 * test1)
        wholeSAS_HET.append(2 * test * test1)

    # if [-1]==0 that means it is a ./. absent allele data, so i inputed 0 as a NaN
    if wholeSIB_AN[-1] == 0:
        wholeSIB_HOMO_ALT.append('NaN')
        wholeSIB_HOMO_REF.append('NaN')
        wholeSIB_HET.append('NaN')
        wholeSIB_AF.append('NaN')
    elif wholeSIB_AN[-1] != 0:
        test = (wholeSIB_AC[-1]) / (wholeSIB_AN[-1])
        wholeSIB_AF.append(test)
        wholeSIB_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeSIB_HOMO_REF.append(test1 * test1)
        wholeSIB_HET.append(2 * test * test1)

    if wholeACB_AN[-1] == 0:
        wholeACB_HOMO_ALT.append('NaN')
        wholeACB_HOMO_REF.append('NaN')
        wholeACB_HET.append('NaN')
        wholeACB_AF.append('NaN')
    elif wholeACB_AN[-1] != 0:
        test = (wholeACB_AC[-1]) / (wholeACB_AN[-1])
        wholeACB_AF.append(test)
        wholeACB_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeACB_HOMO_REF.append(test1 * test1)
        wholeACB_HET.append(2 * test * test1)

    if wholeASW_AN[-1] == 0:
        wholeASW_HOMO_ALT.append('NaN')
        wholeASW_HOMO_REF.append('NaN')
        wholeASW_HET.append('NaN')
        wholeASW_AF.append('NaN')
    elif wholeASW_AN[-1] != 0:
        test = (wholeASW_AC[-1]) / (wholeASW_AN[-1])
        wholeASW_AF.append(test)
        wholeASW_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeASW_HOMO_REF.append(test1 * test1)
        wholeASW_HET.append(2 * test * test1)

    if wholeESN_AN[-1] == 0:
        wholeESN_HOMO_ALT.append('NaN')
        wholeESN_HOMO_REF.append('NaN')
        wholeESN_HET.append('NaN')
        wholeESN_AF.append('NaN')
    elif wholeESN_AN[-1] != 0:
        test = (wholeESN_AC[-1]) / (wholeESN_AN[-1])
        wholeESN_AF.append(test)
        wholeESN_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeESN_HOMO_REF.append(test1 * test1)
        wholeESN_HET.append(2 * test * test1)

    if wholeGWD_AN[-1] == 0:
        wholeGWD_HOMO_ALT.append('NaN')
        wholeGWD_HOMO_REF.append('NaN')
        wholeGWD_HET.append('NaN')
        wholeGWD_AF.append('NaN')
    elif wholeGWD_AN[-1] != 0:
        test = (wholeGWD_AC[-1]) / (wholeGWD_AN[-1])
        wholeGWD_AF.append(test)
        wholeGWD_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeGWD_HOMO_REF.append(test1 * test1)
        wholeGWD_HET.append(2 * test * test1)

    if wholeLWK_AN[-1] == 0:
        wholeLWK_HOMO_ALT.append('NaN')
        wholeLWK_HOMO_REF.append('NaN')
        wholeLWK_HET.append('NaN')
        wholeLWK_AF.append('NaN')
    elif wholeLWK_AN[-1] != 0:
        test = (wholeLWK_AC[-1]) / (wholeLWK_AN[-1])
        wholeLWK_AF.append(test)
        wholeLWK_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeLWK_HOMO_REF.append(test1 * test1)
        wholeLWK_HET.append(2 * test * test1)

    if wholeMSL_AN[-1] == 0:
        wholeMSL_HOMO_ALT.append('NaN')
        wholeMSL_HOMO_REF.append('NaN')
        wholeMSL_HET.append('NaN')
        wholeMSL_AF.append('NaN')
    elif wholeMSL_AN[-1] != 0:
        test = (wholeMSL_AC[-1]) / (wholeMSL_AN[-1])
        wholeMSL_AF.append(test)
        wholeMSL_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeMSL_HOMO_REF.append(test1 * test1)
        wholeMSL_HET.append(2 * test * test1)

    if wholeYRI_AN[-1] == 0:
        wholeYRI_HOMO_ALT.append('NaN')
        wholeYRI_HOMO_REF.append('NaN')
        wholeYRI_HET.append('NaN')
        wholeYRI_AF.append('NaN')
    elif wholeYRI_AN[-1] != 0:
        test = (wholeYRI_AC[-1]) / (wholeYRI_AN[-1])
        wholeYRI_AF.append(test)
        wholeYRI_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeYRI_HOMO_REF.append(test1 * test1)
        wholeYRI_HET.append(2 * test * test1)

    if wholeCLM_AN[-1] == 0:
        wholeCLM_HOMO_ALT.append('NaN')
        wholeCLM_HOMO_REF.append('NaN')
        wholeCLM_HET.append('NaN')
        wholeCLM_AF.append('NaN')
    elif wholeCLM_AN[-1] != 0:
        test = (wholeCLM_AC[-1]) / (wholeCLM_AN[-1])
        wholeCLM_AF.append(test)
        wholeCLM_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeCLM_HOMO_REF.append(test1 * test1)
        wholeCLM_HET.append(2 * test * test1)

    if wholeMXL_AN[-1] == 0:
        wholeMXL_HOMO_ALT.append('NaN')
        wholeMXL_HOMO_REF.append('NaN')
        wholeMXL_HET.append('NaN')
        wholeMXL_AF.append('NaN')
    elif wholeMXL_AN[-1] != 0:
        test = (wholeMXL_AC[-1]) / (wholeMXL_AN[-1])
        wholeMXL_AF.append(test)
        wholeMXL_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeMXL_HOMO_REF.append(test1 * test1)
        wholeMXL_HET.append(2 * test * test1)

    if wholePEL_AN[-1] == 0:
        wholePEL_HOMO_ALT.append('NaN')
        wholePEL_HOMO_REF.append('NaN')
        wholePEL_HET.append('NaN')
        wholePEL_AF.append('NaN')
    elif wholePEL_AN[-1] != 0:
        test = (wholePEL_AC[-1]) / (wholePEL_AN[-1])
        wholePEL_AF.append(test)
        wholePEL_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholePEL_HOMO_REF.append(test1 * test1)
        wholePEL_HET.append(2 * test * test1)

    if wholePUR_AN[-1] == 0:
        wholePUR_HOMO_ALT.append('NaN')
        wholePUR_HOMO_REF.append('NaN')
        wholePUR_HET.append('NaN')
        wholePUR_AF.append('NaN')
    elif wholePUR_AN[-1] != 0:
        test = (wholePUR_AC[-1]) / (wholePUR_AN[-1])
        wholePUR_AF.append(test)
        wholePUR_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholePUR_HOMO_REF.append(test1 * test1)
        wholePUR_HET.append(2 * test * test1)

    if wholeCDX_AN[-1] == 0:
        wholeCDX_HOMO_ALT.append('NaN')
        wholeCDX_HOMO_REF.append('NaN')
        wholeCDX_HET.append('NaN')
        wholeCDX_AF.append('NaN')
    elif wholeCDX_AN[-1] != 0:
        test = (wholeCDX_AC[-1]) / (wholeCDX_AN[-1])
        wholeCDX_AF.append(test)
        wholeCDX_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeCDX_HOMO_REF.append(test1 * test1)
        wholeCDX_HET.append(2 * test * test1)

    if wholeCHB_AN[-1] == 0:
        wholeCHB_HOMO_ALT.append('NaN')
        wholeCHB_HOMO_REF.append('NaN')
        wholeCHB_HET.append('NaN')
        wholeCHB_AF.append('NaN')
    elif wholeCHB_AN[-1] != 0:
        test = (wholeCHB_AC[-1]) / (wholeCHB_AN[-1])
        wholeCHB_AF.append(test)
        wholeCHB_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeCHB_HOMO_REF.append(test1 * test1)
        wholeCHB_HET.append(2 * test * test1)

    if wholeCHS_AN[-1] == 0:
        wholeCHS_HOMO_ALT.append('NaN')
        wholeCHS_HOMO_REF.append('NaN')
        wholeCHS_HET.append('NaN')
        wholeCHS_AF.append('NaN')
    elif wholeCHS_AN[-1] != 0:
        test = (wholeCHS_AC[-1]) / (wholeCHS_AN[-1])
        wholeCHS_AF.append(test)
        wholeCHS_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeCHS_HOMO_REF.append(test1 * test1)
        wholeCHS_HET.append(2 * test * test1)

    if wholeJPT_AN[-1] == 0:
        wholeJPT_HOMO_ALT.append('NaN')
        wholeJPT_HOMO_REF.append('NaN')
        wholeJPT_HET.append('NaN')
        wholeJPT_AF.append('NaN')
    elif wholeJPT_AN[-1] != 0:
        test = (wholeJPT_AC[-1]) / (wholeJPT_AN[-1])
        wholeJPT_AF.append(test)
        wholeJPT_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeJPT_HOMO_REF.append(test1 * test1)
        wholeJPT_HET.append(2 * test * test1)

    if wholeKHV_AN[-1] == 0:
        wholeKHV_HOMO_ALT.append('NaN')
        wholeKHV_HOMO_REF.append('NaN')
        wholeKHV_HET.append('NaN')
        wholeKHV_AF.append('NaN')
    elif wholeKHV_AN[-1] != 0:
        test = (wholeKHV_AC[-1]) / (wholeKHV_AN[-1])
        wholeKHV_AF.append(test)
        wholeKHV_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeKHV_HOMO_REF.append(test1 * test1)
        wholeKHV_HET.append(2 * test * test1)

    if wholeCEU_AN[-1] == 0:
        wholeCEU_HOMO_ALT.append('NaN')
        wholeCEU_HOMO_REF.append('NaN')
        wholeCEU_HET.append('NaN')
        wholeCEU_AF.append('NaN')
    elif wholeCEU_AN[-1] != 0:
        test = (wholeCEU_AC[-1]) / (wholeCEU_AN[-1])
        wholeCEU_AF.append(test)
        wholeCEU_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeCEU_HOMO_REF.append(test1 * test1)
        wholeCEU_HET.append(2 * test * test1)

    if wholeFIN_AN[-1] == 0:
        wholeFIN_HOMO_ALT.append('NaN')
        wholeFIN_HOMO_REF.append('NaN')
        wholeFIN_HET.append('NaN')
        wholeFIN_AF.append('NaN')
    elif wholeFIN_AN[-1] != 0:
        test = (wholeFIN_AC[-1]) / (wholeFIN_AN[-1])
        wholeFIN_AF.append(test)
        wholeFIN_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeFIN_HOMO_REF.append(test1 * test1)
        wholeFIN_HET.append(2 * test * test1)

    if wholeGBR_AN[-1] == 0:
        wholeGBR_HOMO_ALT.append('NaN')
        wholeGBR_HOMO_REF.append('NaN')
        wholeGBR_HET.append('NaN')
        wholeGBR_AF.append('NaN')
    elif wholeGBR_AN[-1] != 0:
        test = (wholeGBR_AC[-1]) / (wholeGBR_AN[-1])
        wholeGBR_AF.append(test)
        wholeGBR_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeGBR_HOMO_REF.append(test1 * test1)
        wholeGBR_HET.append(2 * test * test1)

    if wholeIBS_AN[-1] == 0:
        wholeIBS_HOMO_ALT.append('NaN')
        wholeIBS_HOMO_REF.append('NaN')
        wholeIBS_HET.append('NaN')
        wholeIBS_AF.append('NaN')
    elif wholeIBS_AN[-1] != 0:
        test = (wholeIBS_AC[-1]) / (wholeIBS_AN[-1])
        wholeIBS_AF.append(test)
        wholeIBS_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeIBS_HOMO_REF.append(test1 * test1)
        wholeIBS_HET.append(2 * test * test1)

    if wholeTSI_AN[-1] == 0:
        wholeTSI_HOMO_ALT.append('NaN')
        wholeTSI_HOMO_REF.append('NaN')
        wholeTSI_HET.append('NaN')
        wholeTSI_AF.append('NaN')
    elif wholeTSI_AN[-1] != 0:
        test = (wholeTSI_AC[-1]) / (wholeTSI_AN[-1])
        wholeTSI_AF.append(test)
        wholeTSI_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeTSI_HOMO_REF.append(test1 * test1)
        wholeTSI_HET.append(2 * test * test1)

    if wholeBEB_AN[-1] == 0:
        wholeBEB_HOMO_ALT.append('NaN')
        wholeBEB_HOMO_REF.append('NaN')
        wholeBEB_HET.append('NaN')
        wholeBEB_AF.append('NaN')
    elif wholeBEB_AN[-1] != 0:
        test = (wholeBEB_AC[-1]) / (wholeBEB_AN[-1])
        wholeBEB_AF.append(test)
        wholeBEB_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeBEB_HOMO_REF.append(test1 * test1)
        wholeBEB_HET.append(2 * test * test1)

    if wholeGIH_AN[-1] == 0:
        wholeGIH_HOMO_ALT.append('NaN')
        wholeGIH_HOMO_REF.append('NaN')
        wholeGIH_HET.append('NaN')
        wholeGIH_AF.append('NaN')
    elif wholeGIH_AN[-1] != 0:
        test = (wholeGIH_AC[-1]) / (wholeGIH_AN[-1])
        wholeGIH_AF.append(test)
        wholeGIH_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeGIH_HOMO_REF.append(test1 * test1)
        wholeGIH_HET.append(2 * test * test1)

    if wholeITU_AN[-1] == 0:
        wholeITU_HOMO_ALT.append('NaN')
        wholeITU_HOMO_REF.append('NaN')
        wholeITU_HET.append('NaN')
        wholeITU_AF.append('NaN')
    elif wholeITU_AN[-1] != 0:
        test = (wholeITU_AC[-1]) / (wholeITU_AN[-1])
        wholeITU_AF.append(test)
        wholeITU_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeITU_HOMO_REF.append(test1 * test1)
        wholeITU_HET.append(2 * test * test1)

    if wholePJL_AN[-1] == 0:
        wholePJL_HOMO_ALT.append('NaN')
        wholePJL_HOMO_REF.append('NaN')
        wholePJL_HET.append('NaN')
        wholePJL_AF.append('NaN')
    elif wholePJL_AN[-1] != 0:
        test = (wholePJL_AC[-1]) / (wholePJL_AN[-1])
        wholePJL_AF.append(test)
        wholePJL_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholePJL_HOMO_REF.append(test1 * test1)
        wholePJL_HET.append(2 * test * test1)

    if wholeSTU_AN[-1] == 0:
        wholeSTU_HOMO_ALT.append('NaN')
        wholeSTU_HOMO_REF.append('NaN')
        wholeSTU_HET.append('NaN')
        wholeSTU_AF.append('NaN')
    elif wholeSTU_AN[-1] != 0:
        test = (wholeSTU_AC[-1]) / (wholeSTU_AN[-1])
        wholeSTU_AF.append(test)
        wholeSTU_HOMO_ALT.append(test * test)
        test1 = 1 - test
        wholeSTU_HOMO_REF.append(test1 * test1)
        wholeSTU_HET.append(2 * test * test1)

    formatcounter=formatcounter+1

print(wholeGBR_AN)
print(wholeGBR_AF)
print(wholeGBR_HET)

print(wholeAFR_AN)
print(wholeAFR_AF)
print(wholeAFR_HOMO_ALT)
print(wholeAFR_HOMO_REF)
print(wholeAFR_HET)







# print(wholeSIB_AN) #NOT FREQ # total number of alleles in the format[x], counts 0|0 as 2 alleles and 0|1 as 2 and 1|0 as 2 and 1|1 as 2
# print(wholeSIB_AC) #NOT FREQ # total allele count of alternative allele (1) in format[x], counts 0|0 as 0 and 0|1 as 1 and 1|0 as 1 and 1|1 as 2
# print(wholeSIB_AF)
# print(wholeSIB_HOMO_REF) #total genotype count NOT frequency of reference gt 0|0, counts 0|0 as 1 and rest as 0
# print(wholeSIB_HOMO_ALT) #total genotype count NOT frequency of alternative gt 1|1, counts 1|1 as 1 and rest as 0
# print(wholeSIB_HET) #total genotype count NOT frequency of alternative gt 1|0 or 0|1, counts 0|1 as 1 and 1|0 as 1 and rest as 0
# to calculate GT frequency for example wholeGIH_HOMO_REF, do wholeGIH_HOMO_REF/total number of genotypes: wholeGIH_HOMO_REF/wholeGIH_HOMO_REF+wholeGIH_HOMO_ALT+wholeGIH_HET
# the above is the ACTUAL GT frequency for HOMOZYGOTE REFERENCE for the GIH population
# but for a predicted(???) GT frequency i THINK u can do the ALLELE frequency for ALT allele in XYZ population and SQUARE it, but im not sure
# might have to ask matteo about that???
# i THINK i have to do a predicted(??) GT frequency using the allele frequencies in hardy weinberg equation because this gets u the
# PROBABILITY of each GT freqeuncies whereas the ACTUAL GT frequencies might be random due to chance/luck
# there are certain factors that need to be met for the HWE such as random mating, no migration, no selection, no mutation,
# #and a large population size therefore because these factors are not controlled, the ACTUAL GT frequencies of a given
# population will be different than the predicted(???) GT frequencies when calculated using the allele frequency p^2, q^2, 2pq stuff
#
#
# TL:DR, use predicted GT frequency to calculate GT frequecies because the observed GT freqeuncy will be slightly biased due to luck/other factors
# the predicted GT frequency is calculated using the allele frequencies and doing the p^2, q^2 and 2pq


#ALREADY WROTE AN OUTFILE, DONT REDO UNLESS U WANT TO OVERWRITE


# ###################################################################################################################################################################
# ########################################              WRITING THE DATA INTO A CSV FILE           ##################################################################
# ###################################################################################################################################################################
#
# outfile=open('POPULATION_SNP_FREQEUNCIES.csv', 'w', newline='') #creates a csv file and stores it into outfile variable
# writer=csv.writer(outfile) #creates a variable to store writing data
# rows=['','','','','','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AFR','AMR','AMR','AMR','AMR','AMR','AMR','AMR','AMR','AMR','AMR','AMR','AMR','AMR','AMR','AMR','AMR','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EAS','EUR','EUR','EUR','EUR','EUR','EUR','EUR','EUR','EUR','EUR','EUR','EUR','EUR','EUR','EUR','EUR','EUR','EUR','EUR','EUR','SAS','SAS','SAS','SAS','SAS','SAS','SAS','SAS','SAS','SAS','SAS','SAS','SAS','SAS','SAS','SAS','SAS','SAS','SAS','SAS',]
# writer.writerow(rows)
# rows=['SNP_ID','SIB_ALT_ALLELE_FREQ','SIB_HOMOZYGOUS_ALT_GT_FREQ', 'SIB_HOMOZYGOUS_REF_GT_FREQ', 'SIB_HETEROZYGOUS_GT_FREQ','ACB_ALT_ALLELE_FREQ','ACB_HOMOZYGOUS_ALT_GT_FREQ', 'ACB_HOMOZYGOUS_REF_GT_FREQ', 'ACB_HETEROZYGOUS_GT_FREQ','ASW_ALT_ALLELE_FREQ','ASW_HOMOZYGOUS_ALT_GT_FREQ', 'ASW_HOMOZYGOUS_REF_GT_FREQ', 'ASW_HETEROZYGOUS_GT_FREQ','ESN_ALT_ALLELE_FREQ','ESN_HOMOZYGOUS_ALT_GT_FREQ', 'ESN_HOMOZYGOUS_REF_GT_FREQ', 'ESN_HETEROZYGOUS_GT_FREQ','GWD_ALT_ALLELE_FREQ','GWD_HOMOZYGOUS_ALT_GT_FREQ', 'GWD_HOMOZYGOUS_REF_GT_FREQ', 'GWD_HETEROZYGOUS_GT_FREQ','LWK_ALT_ALLELE_FREQ','LWK_HOMOZYGOUS_ALT_GT_FREQ', 'LWK_HOMOZYGOUS_REF_GT_FREQ', 'LWK_HETEROZYGOUS_GT_FREQ','MSL_ALT_ALLELE_FREQ','MSL_HOMOZYGOUS_ALT_GT_FREQ', 'MSL_HOMOZYGOUS_REF_GT_FREQ', 'MSL_HETEROZYGOUS_GT_FREQ','YRI_ALT_ALLELE_FREQ','YRI_HOMOZYGOUS_ALT_GT_FREQ', 'YRI_HOMOZYGOUS_REF_GT_FREQ', 'YRI_HETEROZYGOUS_GT_FREQ','CLM_ALT_ALLELE_FREQ','CLM_HOMOZYGOUS_ALT_GT_FREQ', 'CLM_HOMOZYGOUS_REF_GT_FREQ', 'CLM_HETEROZYGOUS_GT_FREQ','MXL_ALT_ALLELE_FREQ','MXL_HOMOZYGOUS_ALT_GT_FREQ', 'MXL_HOMOZYGOUS_REF_GT_FREQ', 'MXL_HETEROZYGOUS_GT_FREQ','PEL_ALT_ALLELE_FREQ','PEL_HOMOZYGOUS_ALT_GT_FREQ', 'PEL_HOMOZYGOUS_REF_GT_FREQ', 'PEL_HETEROZYGOUS_GT_FREQ','PUR_ALT_ALLELE_FREQ','PUR_HOMOZYGOUS_ALT_GT_FREQ', 'PUR_HOMOZYGOUS_REF_GT_FREQ', 'PUR_HETEROZYGOUS_GT_FREQ','CDX_ALT_ALLELE_FREQ','CDX_HOMOZYGOUS_ALT_GT_FREQ', 'CDX_HOMOZYGOUS_REF_GT_FREQ', 'CDX_HETEROZYGOUS_GT_FREQ','CHB_ALT_ALLELE_FREQ','CHB_HOMOZYGOUS_ALT_GT_FREQ', 'CHB_HOMOZYGOUS_REF_GT_FREQ', 'CHB_HETEROZYGOUS_GT_FREQ','CHS_ALT_ALLELE_FREQ','CHS_HOMOZYGOUS_ALT_GT_FREQ', 'CHS_HOMOZYGOUS_REF_GT_FREQ', 'CHS_HETEROZYGOUS_GT_FREQ','JPT_ALT_ALLELE_FREQ','JPT_HOMOZYGOUS_ALT_GT_FREQ', 'JPT_HOMOZYGOUS_REF_GT_FREQ', 'JPT_HETEROZYGOUS_GT_FREQ','KHV_ALT_ALLELE_FREQ','KHV_HOMOZYGOUS_ALT_GT_FREQ', 'KHV_HOMOZYGOUS_REF_GT_FREQ', 'KHV_HETEROZYGOUS_GT_FREQ','CEU_ALT_ALLELE_FREQ','CEU_HOMOZYGOUS_ALT_GT_FREQ', 'CEU_HOMOZYGOUS_REF_GT_FREQ', 'CEU_HETEROZYGOUS_GT_FREQ','FIN_ALT_ALLELE_FREQ','FIN_HOMOZYGOUS_ALT_GT_FREQ', 'FIN_HOMOZYGOUS_REF_GT_FREQ', 'FIN_HETEROZYGOUS_GT_FREQ','GBR_ALT_ALLELE_FREQ','GBR_HOMOZYGOUS_ALT_GT_FREQ', 'GBR_HOMOZYGOUS_REF_GT_FREQ', 'GBR_HETEROZYGOUS_GT_FREQ','IBS_ALT_ALLELE_FREQ','IBS_HOMOZYGOUS_ALT_GT_FREQ', 'IBS_HOMOZYGOUS_REF_GT_FREQ', 'IBS_HETEROZYGOUS_GT_FREQ','TSI_ALT_ALLELE_FREQ','TSI_HOMOZYGOUS_ALT_GT_FREQ', 'TSI_HOMOZYGOUS_REF_GT_FREQ', 'TSI_HETEROZYGOUS_GT_FREQ','BEB_ALT_ALLELE_FREQ','BEB_HOMOZYGOUS_ALT_GT_FREQ', 'BEB_HOMOZYGOUS_REF_GT_FREQ', 'BEB_HETEROZYGOUS_GT_FREQ','GIH_ALT_ALLELE_FREQ','GIH_HOMOZYGOUS_ALT_GT_FREQ', 'GIH_HOMOZYGOUS_REF_GT_FREQ', 'GIH_HETEROZYGOUS_GT_FREQ', 'ITU_ALT_ALLELE_FREQ','ITU_HOMOZYGOUS_ALT_GT_FREQ', 'ITU_HOMOZYGOUS_REF_GT_FREQ', 'ITU_HETEROZYGOUS_GT_FREQ','PJL_ALT_ALLELE_FREQ','PJL_HOMOZYGOUS_ALT_GT_FREQ', 'PJL_HOMOZYGOUS_REF_GT_FREQ', 'PJL_HETEROZYGOUS_GT_FREQ','STU_ALT_ALLELE_FREQ','STU_HOMOZYGOUS_ALT_GT_FREQ', 'STU_HOMOZYGOUS_REF_GT_FREQ', 'STU_HETEROZYGOUS_GT_FREQ',]
# writer.writerow(rows) #writing the columns of the csv by using the columns in my Person database
#
# csvcounter=0
# for x in wholeSIB_AF:
#     test=(snpidlist[csvcounter],wholeSIB_AF[csvcounter],wholeSIB_HOMO_ALT[csvcounter],wholeSIB_HOMO_REF[csvcounter],wholeSIB_HET[csvcounter],wholeACB_AF[csvcounter],wholeACB_HOMO_ALT[csvcounter],wholeACB_HOMO_REF[csvcounter],wholeACB_HET[csvcounter],wholeASW_AF[csvcounter],wholeASW_HOMO_ALT[csvcounter],wholeASW_HOMO_REF[csvcounter],wholeASW_HET[csvcounter],wholeESN_AF[csvcounter],wholeESN_HOMO_ALT[csvcounter],wholeESN_HOMO_REF[csvcounter],wholeESN_HET[csvcounter],wholeGWD_AF[csvcounter],wholeGWD_HOMO_ALT[csvcounter],wholeGWD_HOMO_REF[csvcounter],wholeGWD_HET[csvcounter],wholeLWK_AF[csvcounter],wholeLWK_HOMO_ALT[csvcounter],wholeLWK_HOMO_REF[csvcounter],wholeLWK_HET[csvcounter],wholeMSL_AF[csvcounter],wholeMSL_HOMO_ALT[csvcounter],wholeMSL_HOMO_REF[csvcounter],wholeMSL_HET[csvcounter],wholeYRI_AF[csvcounter],wholeYRI_HOMO_ALT[csvcounter],wholeYRI_HOMO_REF[csvcounter],wholeYRI_HET[csvcounter],wholeCLM_AF[csvcounter],wholeCLM_HOMO_ALT[csvcounter],wholeCLM_HOMO_REF[csvcounter],wholeCLM_HET[csvcounter],wholeMXL_AF[csvcounter],wholeMXL_HOMO_ALT[csvcounter],wholeMXL_HOMO_REF[csvcounter],wholeMXL_HET[csvcounter],wholePEL_AF[csvcounter],wholePEL_HOMO_ALT[csvcounter],wholePEL_HOMO_REF[csvcounter],wholePEL_HET[csvcounter],wholePUR_AF[csvcounter],wholePUR_HOMO_ALT[csvcounter],wholePUR_HOMO_REF[csvcounter],wholePUR_HET[csvcounter],wholeCDX_AF[csvcounter],wholeCDX_HOMO_ALT[csvcounter],wholeCDX_HOMO_REF[csvcounter],wholeCDX_HET[csvcounter],wholeCHB_AF[csvcounter],wholeCHB_HOMO_ALT[csvcounter],wholeCHB_HOMO_REF[csvcounter],wholeCHB_HET[csvcounter],wholeCHS_AF[csvcounter],wholeCHS_HOMO_ALT[csvcounter],wholeCHS_HOMO_REF[csvcounter],wholeCHS_HET[csvcounter],wholeJPT_AF[csvcounter],wholeJPT_HOMO_ALT[csvcounter],wholeJPT_HOMO_REF[csvcounter],wholeJPT_HET[csvcounter],wholeKHV_AF[csvcounter],wholeKHV_HOMO_ALT[csvcounter],wholeKHV_HOMO_REF[csvcounter],wholeKHV_HET[csvcounter],wholeCEU_AF[csvcounter],wholeCEU_HOMO_ALT[csvcounter],wholeCEU_HOMO_REF[csvcounter],wholeCEU_HET[csvcounter],wholeFIN_AF[csvcounter],wholeFIN_HOMO_ALT[csvcounter],wholeFIN_HOMO_REF[csvcounter],wholeFIN_HET[csvcounter],wholeGBR_AF[csvcounter],wholeGBR_HOMO_ALT[csvcounter],wholeGBR_HOMO_REF[csvcounter],wholeGBR_HET[csvcounter],wholeIBS_AF[csvcounter],wholeIBS_HOMO_ALT[csvcounter],wholeIBS_HOMO_REF[csvcounter],wholeIBS_HET[csvcounter],wholeTSI_AF[csvcounter],wholeTSI_HOMO_ALT[csvcounter],wholeTSI_HOMO_REF[csvcounter],wholeTSI_HET[csvcounter],wholeBEB_AF[csvcounter],wholeBEB_HOMO_ALT[csvcounter],wholeBEB_HOMO_REF[csvcounter],wholeBEB_HET[csvcounter],wholeGIH_AF[csvcounter],wholeGIH_HOMO_ALT[csvcounter],wholeGIH_HOMO_REF[csvcounter],wholeGIH_HET[csvcounter],wholeITU_AF[csvcounter],wholeITU_HOMO_ALT[csvcounter],wholeITU_HOMO_REF[csvcounter],wholeITU_HET[csvcounter],wholePJL_AF[csvcounter],wholePJL_HOMO_ALT[csvcounter],wholePJL_HOMO_REF[csvcounter],wholePJL_HET[csvcounter],wholeSTU_AF[csvcounter],wholeSTU_HOMO_ALT[csvcounter],wholeSTU_HOMO_REF[csvcounter],wholeSTU_HET[csvcounter],)
#     writer.writerow(test)
#     csvcounter=csvcounter+1
#
# outfile.close()

#ALREADY WROTE TO FILE DONT DO AGAIN UNLESS U WANT TO OVERWRITE EXISTING DATA WITH NEW ONE
#ALREADY WROTE TO FILE DONT DO AGAIN UNLESS U WANT TO OVERWRITE EXISTING DATA WITH NEW ONE

# #####WRITING SUPER CONTINENT DATA INTO CSV FILE
# outfile=open('SUPERCONTINENT_SNP_FREQUENCIES.csv', 'w', newline='')
# writer = csv.writer(outfile)
# rows=['SNP_ID', 'AFR_ALT_ALLELE FREQ', 'AFR_HOMOZYGOUS_ALT_GT_FREQ', 'AFR_HOMOZYGOUS_REF_GT_FREQ', 'AFR_HETEROZYGOUS_GT_FREQ','AMR_ALT_ALLELE FREQ', 'AMR_HOMOZYGOUS_ALT_GT_FREQ', 'AMR_HOMOZYGOUS_REF_GT_FREQ', 'AMR_HETEROZYGOUS_GT_FREQ','EAS_ALT_ALLELE FREQ', 'EAS_HOMOZYGOUS_ALT_GT_FREQ', 'EAS_HOMOZYGOUS_REF_GT_FREQ', 'EAS_HETEROZYGOUS_GT_FREQ','EUR_ALT_ALLELE FREQ', 'EUR_HOMOZYGOUS_ALT_GT_FREQ', 'EUR_HOMOZYGOUS_REF_GT_FREQ', 'EUR_HETEROZYGOUS_GT_FREQ','SAS_ALT_ALLELE FREQ', 'SAS_HOMOZYGOUS_ALT_GT_FREQ', 'SAS_HOMOZYGOUS_REF_GT_FREQ', 'SAS_HETEROZYGOUS_GT_FREQ']
# writer.writerow(rows)
# csvcounter=0
# for x in wholeSIB_AF:
#     test=(snpidlist[csvcounter], wholeAFR_AF[csvcounter], wholeAFR_HOMO_ALT[csvcounter], wholeAFR_HOMO_REF[csvcounter], wholeAFR_HET[csvcounter],wholeAMR_AF[csvcounter], wholeAMR_HOMO_ALT[csvcounter], wholeAMR_HOMO_REF[csvcounter], wholeAMR_HET[csvcounter],wholeEAS_AF[csvcounter], wholeEAS_HOMO_ALT[csvcounter], wholeEAS_HOMO_REF[csvcounter], wholeEAS_HET[csvcounter],wholeEUR_AF[csvcounter], wholeEUR_HOMO_ALT[csvcounter], wholeEUR_HOMO_REF[csvcounter], wholeEUR_HET[csvcounter],wholeSAS_AF[csvcounter], wholeSAS_HOMO_ALT[csvcounter], wholeSAS_HOMO_REF[csvcounter], wholeSAS_HET[csvcounter])
#     writer.writerow(test)
#     csvcounter=csvcounter+1
# outfile.close