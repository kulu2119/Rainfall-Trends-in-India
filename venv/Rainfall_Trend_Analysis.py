# importing pandas module 
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import plotly.express as px
# loading csv file 
rain_data=pd.read_csv(r"C:\Users\kulde\Data_Science Projects\Rainfall Trends in India\venv\rainfall_area-wt_India_1901-2015.csv")
#rain_data.info()
# Graph to visualize the Year on Year trend of the Rainfall  
rain_fall_YOY=rain_data[['YEAR','ANNUAL']]
Rain_fall_annual_mean=rain_data['ANNUAL'].mean()
#plt.figure(figsize=(15,12),dpi=150)
#sn.lineplot(data=rain_fall_YOY,x='YEAR',y='ANNUAL',markers='o',label='Annual Rainfall')
#plt.axhline(Rain_fall_annual_mean,color='red',linestyle='--',label=f"Mean Rainfall ({Rain_fall_annual_mean:.2f})")
fig=px.line(rain_fall_YOY,x='YEAR',y='ANNUAL',title='TREND OF ANNUAL RAINFALL IN INDIA(1900 - 2015) ',markers=True)
fig.add_hline(y=Rain_fall_annual_mean,line_dash="dash",line_color="red",annotation_text=f'Mean RAinfall:{Rain_fall_annual_mean:.2f}',annotation_position='top left')
fig.show()

#Graph to visualize the MOM trend of the average Rainfall 
monthly_columns = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
monthly_avg=rain_data[monthly_columns].mean()
fig1=px.bar(x=monthly_avg.index,y=monthly_avg.values,labels={'x':'Month','y':'Rainfall (mm)'},title='Average monthly rainfall in India (1901 - 2015)',text=monthly_avg.values)
fig1.add_hline(y=monthly_avg.mean(),line_dash='dash',line_color='red',annotation_text=f'Mean Rainfall',annotation_position='top left')
fig1.show()
highest_rainfallmonth=monthly_avg.idxmax()
lowese_rainfallmonth=monthly_avg.idxmin()

# graph to visualize the seasonal trend of the avearge rainfall
seasonal_columns = ['Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec']
seasonal_avg=rain_data[seasonal_columns].mean()
seasonal_avg
fig2=px.bar(x=seasonal_avg.index,y=seasonal_avg.values,labels={'x':'Seasons','y':'RainFall (nm)'},title='Average Seasonal Rainfall in India',text=seasonal_avg.values,color=seasonal_avg.values,color_continuous_scale=['gold', 'skyblue', 'green', 'orange'])
fig2.add_hline(y=seasonal_avg.mean(),line_dash='dash',line_color='red',annotation_text='Mean RainFall',annotation_position='top left')
fig2.show()