from django.core.management import BaseCommand
import pandas as pd

class Command(BaseCommand):
    def handle(self,*args,**option):
        path = '/mnt/c/Users/User/Downloads/SNS_Activewear_DataLibrary'
        product_path = path + '/Products.xlsx'
        df = pd.read_excel(product_path,sheet_name='Sheet1',index_col='sku')
        uniques = df.brandName.unique()
        print(uniques)

        # with pd.ExcelWriter('District_Data.xlsx') as writer:
        #     for District in uniques:
        #         df[df.District == District].to_excel(writer, index=None, sheet_name=District)

        

if __name__ == '__main__':
    dat = Command()
    dat.handle()