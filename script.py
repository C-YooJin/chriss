import mysql.connector
from mysql.connector import Error
import pandas as pd
import numpy as np

def Excel_Out(connection, startDt, endDt):
    try:
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor(dictionary=True)

            query_total = ("SELECT InputDate, Investigator_date, Investigator_phone, Investigator_name,"
                     "Subject_gender, Subject_reg_number, Subject_job, "
                     "InspectionCaseNm, Doctor_type1_nm, Suspicion, Suspicion_category_overseas, "
                     "Suspicion_category_gangnam, Subject_address, Travel_status, Travel_leave_date, "
                     "Travel_visit1_country, Travel_visit1_city, Travel_visit1_start_date, Travel_visit1_end_date, "
                     "Travel_transit_status, Travel_transit_country, Travel_transit_city, Travel_trasit_start_date, "
                     "Travel_transit_end_date, Travel_reason_nm, Travel_partner_count_nm, Travel_other_nm, Travel_entry_date, "
                     "Travel_entry_flight, Symptom_first_nm, Symptom_first_date, Symptom_first_area_nm, "
                     "Symptom_first_diagnosis_nm, Symptom_now_nm, Medicine_status, Medicine_smoke_status, Base_disease_status, "
                     "Pregnancy_status, Healthcare_facility_nm, etc_type1_status, etc_type2_status, etc_type3_status, "
                     "etc_type4_famliy_count, etc_type4_doctor_count, etc_type4_company_count, etc_type4_etc_count, "
                     "Suspicion_classification, Suspicion_case, InspectionCaseNm, Doctor_type2_nm, "
                     "Doctor_type3_nm, Doctor_type4_nm, SpecimenDocName, Doctor_date, investigator_affiliation, "
                     "Investigator_name, Investigator_phone, Investigator_root, SpecimenDocMessage, SpecimenDocName "
                     "FROM covid.epidemiology "
                     "WHERE input_date between (%s) and (%s) order by input_date; ")
            cursor.execute(query_total, (startDt, endDt))
            record_total = cursor.fetchall()

            #print("You're connected to database: ", record)
            #print(type(record))
            my_map_total = {"InputDate": "입력일자", "Investigator_date": "조사일자", "Investigator_phone": "핸드폰번호",
                      "Investigator_name": "이름", "Subject_gender": "성별", "Subject_reg_number": "생년월일",
                      "Subject_job": "직업", "InspectionCaseNm": "검사케이스", "Doctor_type1_nm": "사례분류",
                      "Suspicion": "의심경로구분", "Suspicion_category_overseas": "의심경로대구분",
                      "Suspicion_category_gangnam": "의심경로소구분",
                      "Subject_address": "주소", "Travel_status": "해외방문여부", "Travel_leave_date": "출국일시",
                      "Travel_visit1_country": "방문국가", "Travel_visit1_city": "도시명",
                      "Travel_visit1_start_date": "기간(시작)",
                      "Travel_visit1_end_date": "기간(끝)", "Travel_transit_status": "입국시 경유",
                      "Travel_transit_country": "경유국가",
                      "Travel_transit_city": "경유도시", "Travel_trasit_start_date": "경유시작",
                      "Travel_transit_end_date": "경유종료",
                      "Travel_reason_nm": "방문목적", "Travel_partner_count_nm": "동반자", "Travel_other_nm": "감염위험요인",
                      "Travel_entry_date": "입국일시", "Travel_entry_flight": "항공편", "Symptom_first_nm": "임상증상",
                      "Symptom_first_date": "발현일시", "Symptom_first_area_nm": "발현장소",
                      "Symptom_first_diagnosis_nm": "확진자",
                      "Symptom_now_nm": "현재증상", "Medicine_status": "해열제복용여부", "Medicine_smoke_status": "흡연여부",
                      "Base_disease_status": "기저질환", "Pregnancy_status": "임신여부", "Healthcare_facility_nm": "의료기관진단",
                      "etc_type1_status": "입국시 기재여부", "etc_type2_status": "여행력 확인", "etc_type3_status": "1339 수신",
                      "etc_type4_famliy_count": "접촉자(가족)", "etc_type4_doctor_count": "접촉자(의료진)",
                      "etc_type4_company_count": "접촉자(직장)", "etc_type4_etc_count": "접촉자(그외)",
                      "Suspicion_classification": "비고(특기사항)", "Suspicion_case": "검체채취구분", "InspectionCaseNm": "검사케이스",
                      "Doctor_type2_nm": "역학적 연관성", "Doctor_type3_nm": "임상증상", "Doctor_type4_nm": "보건소조치사항",
                      "SpecimenDocName": "담당역학조사관", "Doctor_date": "사례분류일시", "investigator_affiliation": "조사자 소속",
                      "Investigator_name": "조사자 성명", "Investigator_phone": "조사자 연락처", "Investigator_root": "인지경로(기관)",
                      "SpecimenDocMessage": "담당의사소견", "SpecimenDocName": "담당역학조사관"}

            df_total = pd.DataFrame(record_total).rename(columns=my_map_total)

            query_report = ("SELECT InputDate, Investigator_date, Investigator_phone, Investigator_name,"
                           "Subject_gender, Subject_reg_number, Subject_job, "
                           "InspectionCaseNm, Doctor_type1_nm, Suspicion, Suspicion_category_overseas, "
                           "Suspicion_category_gangnam, Subject_address "
                           "FROM covid.epidemiology "
                           "WHERE input_date between (%s) and (%s) order by input_date; ")

            cursor.execute(query_report, (startDt, endDt))
            record_report = cursor.fetchall()

            my_map_report = {"InputDate": "입력일자", "Investigator_date": "조사일자", "Investigator_phone": "핸드폰번호",
                             "Investigator_name": "이름", "Subject_gender": "성별", "Subject_reg_number": "생년월일",
                             "Subject_job": "직업", "InspectionCaseNm": "검사케이스", "Doctor_type1_nm": "사례분류",
                             "Suspicion": "의심경로구분", "Suspicion_category_overseas": "의심경로대구분",
                             "Suspicion_category_gangnam": "의심경로소구분",
                             "Subject_address": "주소"}

            df_report = pd.DataFrame(record_report).rename(columns=my_map_report)


            # Create a Pandas Excel writer using XlsxWriter as the engine
            writer = pd.ExcelWriter('{}to{}_covid.xlsx'.format(startDt, endDt), engine='xlsxwriter')

            # Write each dataframe to a different worksheet.
            df_total.to_excel(writer, sheet_name='전체 데이터')
            df_report.to_excel(writer, sheet_name='보고용 데이터')

            # Close the Pandas Excel writer and output the Excel file.
            writer.save()

        else:
            print("if connection fail")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
        else:
            print("응아니야")