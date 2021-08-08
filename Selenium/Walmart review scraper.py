from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

walmart = webdriver.Chrome(ChromeDriverManager().install())
walmart.get("https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365")
time.sleep(3)


walmart.find_element(By.XPATH,"//span[text()='See all reviews']").click()

walmart.find_element(By.XPATH,"//select[@aria-label='Sort by']/option[3]").click()
time.sleep(5)

end_month = 'december'
end_year = '2020'

reviews_data = pd.DataFrame(columns=['Name','Date','Title','Review','Rating'])

end_condition_status = False

while end_condition_status is False:
    
    review_details = []
   
    for review in walmart.find_elements(By.XPATH,"//div[@itemprop='review']"):

        review_date = review.find_element_by_class_name('review-date-submissionTime').text
        reviewer_name = review.find_element_by_class_name('review-footer-userNickname').text
        review_rating = review.find_element_by_class_name('average-rating').find_elements_by_tag_name('span')[1].text 
        review_body = review.find_element_by_class_name('review-text').text
        
        try:
            review_title = review.find_element_by_tag_name('h3').text

        except NoSuchElementException as exception:
            review_title = ''
            pass
               
        if end_month in review_date.lower() and end_year in review_date:
            end_condition_status = True
            break
        
        else:
            review_details.append([reviewer_name,review_date, review_title,review_body,review_rating])
    
    details = {"data":review_details}
    
    if len(reviews_data)>0:
        reviews_data =  reviews_data.append(pd.DataFrame(details['data'], columns = reviews_data.columns))

    else:
        reviews_data = pd.DataFrame(details['data'], columns = reviews_data.columns)

    walmart.find_element(By.XPATH,"//button[@class='paginator-btn paginator-btn-next']").click()
    time.sleep(5)

reviews_data.index = range(1,len(reviews_data)+1)
    
File_name = 'output.csv'

with open(File_name, 'w', encoding="utf-8") as name:
    reviews_data.to_csv(name, line_terminator='\n')
    
walmart.quit()

print("Scraping completed")
