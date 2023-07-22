DROP TABLE IF EXISTS tb_ktas;
CREATE TABLE "tb_ktas" (
	"ktas_id"	INTEGER,
	"first_category_name"	TEXT NOT NULL,
	"first_category_code"	TEXT NOT NULL,
	"second_category_name"	TEXT NOT NULL,
	"second_category_code"	TEXT NOT NULL,
	"third_category_name"	TEXT NOT NULL,
	"third_category_code"	TEXT NOT NULL,
	"fourth_category_name"	TEXT NOT NULL,
	"fourth_category_code"	TEXT NOT NULL,
	"final_grade"	TEXT NOT NULL,
	"ktas_code"	TEXT NOT NULL,
	PRIMARY KEY("ktas_id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS tb_employee;
CREATE TABLE "tb_employee" (
	"employee_id"	INTEGER,
	"name"	TEXT NOT NULL,
	"type_job"	INTEGER NOT NULL,
	"login_username"	TEXT NOT NULL UNIQUE,
	"login_password"	TEXT NOT NULL,
	"mobile_phone_num_1"	TEXT,
	"mobile_phone_num_2"	TEXT,
	PRIMARY KEY("employee_id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS tb_department;
CREATE TABLE "tb_department" (
    "department_id"	INTEGER,
    "name"	TEXT NOT NULL,
    "job_category"	INTEGER NOT NULL,
    PRIMARY KEY("department_id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS tb_doctor;
CREATE TABLE "tb_doctor" (
	"doctor_id"	INTEGER,
	"employee_id"	INTEGER NOT NULL,
	"assigned_department_id"	INTEGER NOT NULL,
	PRIMARY KEY("doctor_id" AUTOINCREMENT)
	FOREIGN KEY("assigned_department_id") REFERENCES "tb_department"("department_id")
);

DROP TABLE IF EXISTS tb_nurse;
CREATE TABLE "tb_nurse" (
	"nurse_id"	INTEGER,
	"employee_id"	INTEGER NOT NULL,
	"assigned_ward_id"	INTEGER NOT NULL,
	PRIMARY KEY("nurse_id" AUTOINCREMENT),
	FOREIGN KEY("employee_id") REFERENCES "tb_employee"("employee_id")
	FOREIGN KEY("assigned_ward_id") REFERENCES "tb_department"("department_id")
);

DROP TABLE IF EXISTS tb_administration;
CREATE TABLE "tb_administration" (
    "administration_id"	INTEGER,
    "employee_id"	INTEGER NOT NULL,
    "assigned_part_id"	INTEGER NOT NULL,
    PRIMARY KEY("administration_id" AUTOINCREMENT),
    FOREIGN KEY("employee_id") REFERENCES "tb_employee"("employee_id"),
    FOREIGN KEY("assigned_part_id") REFERENCES "tb_department"("department_id")
);
DROP TABLE IF EXISTS tb_chat_room;
CREATE TABLE "tb_chat_room" (
    "chat_room_id"	INTEGER,
    "created_time"	TEXT NOT NULL,
    PRIMARY KEY("chat_room_id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS tb_employee_chat_room;
CREATE TABLE "tb_employee_chat_room" (
	"employee_chat_room_id"	INTEGER,
	"chat_room_id"	INTEGER NOT NULL,
	"employee_id"	INTEGER NOT NULL,
	FOREIGN KEY("chat_room_id") REFERENCES "tb_chat_room"("chat_room_id"),
	FOREIGN KEY("employee_id") REFERENCES "tb_employee"("employee_id"),
	PRIMARY KEY("employee_chat_room_id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS tb_patient;
CREATE TABLE "tb_patient" (
	"patient_id"	INTEGER,
	"birth_date"	TEXT,
	"name"	TEXT NOT NULL,
	"sex"	TEXT NOT NULL,
	"ssn"	TEXT UNIQUE,
	"address"	TEXT,
	"type_insurance"	TEXT,
	"using_bed_id"	INTEGER,
	"register_number"	INTEGER UNIQUE,
	"assigned_doctor_id"	INTEGER,
	"assigned_nurse_id"	INTEGER,
	FOREIGN KEY("using_bed_id") REFERENCES "tb_bed_of_ward"("bed_id"),
	FOREIGN KEY("assigned_doctor_id") REFERENCES "tb_doctor"("doctor_id"),
	FOREIGN KEY("assigned_nurse_id") REFERENCES "tb_nurse"("nurse_id"),
	PRIMARY KEY("patient_id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS tb_bed_of_ward;
CREATE TABLE "tb_bed_of_ward" (
    "bed_id"	INTEGER,
    "assigned_ward_id"	INTEGER NOT NULL,
    "additional_info"	TEXT,
    "viewing_bed_name"	TEXT NOT NULL,
    PRIMARY KEY("bed_id" AUTOINCREMENT),
    FOREIGN KEY("assigned_ward_id") REFERENCES "tb_department"
);

DROP TABLE IF EXISTS tb_emergency_nurse_record;
CREATE TABLE "tb_emergency_nurse_record" (
	"enr_id"	INTEGER,
	"register_id"	INTEGER,
	"onset_time"	TEXT,
	"ktas_id"	INTEGER,
	"cheif_complain"	TEXT,
	"description"	TEXT,
	"recorder_nurse_id"	INTEGER,
	"saved_time"	TEXT,
	"responser"	TEXT,
	"memo"	TEXT,
	PRIMARY KEY("enr_id" AUTOINCREMENT),
	FOREIGN KEY("recorder_nurse_id") REFERENCES "tb_nurse"("nurse_id")
	FOREIGN KEY("register_id") REFERENCES "tb_patient"("register_number")
);



DROP TABLE IF EXISTS tb_message;
CREATE TABLE "tb_message" (
	"message_id"	INTEGER,
	"sender_employee_id"	INTEGER NOT NULL,
	"chat_room_id"	INTEGER NOT NULL,
	"contents"	TEXT NOT NULL,
	"is_confirmed"	INTEGER NOT NULL,
	FOREIGN KEY("chat_room_id") REFERENCES "tb_chat_room"("chat_room_id"),
	PRIMARY KEY("message_id" AUTOINCREMENT),
	FOREIGN KEY("sender_employee_id") REFERENCES "tb_employee"("employee_id")
);

DROP TABLE IF EXISTS tb_medical_order;
CREATE TABLE "tb_medical_order" (
	"medical_order_id"	INTEGER,
	"patient_register_id"	INTEGER NOT NULL,
	"saved_timestamp"	TEXT NOT NULL,
	"order_statement"	TEXT NOT NULL,
	"recoder_doctor_id"	INTEGER NOT NULL,
	FOREIGN KEY("recoder_doctor_id") REFERENCES "tb_doctor"("doctor_id"),
	PRIMARY KEY("medical_order_id" AUTOINCREMENT)
);

INSERT INTO tb_employee("name", "type_job", "login_username", "login_password", "mobile_phone_num_1", "mobile_phone_num_2") values
("박광현", 2, "qqq", "1234", "010-1234-5678","-"),
("노우현", 1, "qq", "1234", "010-2222-5678","-"),
("주혜인", 2, "q123", "1234", "010-4422-5678","-");

INSERT INTO tb_chat_room("created_time") values ("2023-07-22 09:00:00"),("2023-07-21 21:00:00");
INSERT INTO tb_employee_chat_room("chat_room_id","employee_id") values (1, 1),
(1, 2),
(2, 1),
(2, 3);

INSERT INTO tb_message("sender_employee_id","chat_room_id","contents","is_confirmed") values
(1, 1, "ER 김철수님 NRS 7점 chest pain 호소합니다.", 0),
(1, 1, "처방주세요", 0),
(2, 1, "알겠습니다. 처방대로 주세요, 금방 가겠습니다.", 0),
(2, 2, "EDTA 보틀좀 빌려주세요", 0),
(1, 2, "우리도 없어요 죄송", 0);


INSERT INTO tb_nurse('employee_id', 'assigned_ward_id') values
(1, 9);

INSERT INTO tb_doctor('employee_id', 'assigned_department_id') values
(2, 3);

INSERT INTO tb_department("name", "job_category") VALUES
("응급의학과", 1),("신경외과", 1), ("흉부외과", 1), ("외과", 1), ("내과", 1), ("소아청소년과", 1),
("7A",2),("9B",2),("ER",2),("MICU",2),("101W",2),("EICU",2),
("원무과",3),("보험심사팀",3);

INSERT INTO tb_bed_of_ward("assigned_ward_id", "additional_info", "viewing_bed_name") VALUES
(9, "소생실", "CR1"),
(9, "소생실", "CR2"),
(9, "중증구역", "IC1"),
(9, "중증구역", "IC2"),
(9, "중증구역", "IC3"),
(9, "중증구역", "IC4"),
(9, "중증구역", "IC5"),
(9, "중증구역", "IC6"),
(9, "중증구역", "IC7"),
(9, "중증구역", "IC8"),
(9, "중증구역", "IC9"),
(9, "중증구역", "IC10"),
(9, "중증구역", "IC11"),
(9, "중증구역", "IC12"),
(9, "경증구역", "TR");

INSERT INTO tb_patient("birth_date", "name","sex", "ssn", "address", "type_insurance", "using_bed_id", "register_number", "assigned_doctor_id", "assigned_nurse_id") VALUES
('1958-06-08', '김철수', 'M', '580608-1354644', '경기도 수원시 언저리 어딘가', '건강보험', 1, 486124, 1, 1);

INSERT INTO tb_emergency_nurse_record(
    "onset_time",
    "register_id",
    "ktas_id",
    "cheif_complain",
    "description",
    "recorder_nurse_id",
    "saved_time",
    "responser",
    "memo") values
    ('2022-07-18',486124, 'AICAB', '가슴이 답답해요',
"내원전 2시간 전, 속 울렁거림, 가슴 답답함 느껴졌으나 시간 지나니 괜찮아짐, 식사 후 집으로 귀가하던 중 가슴 부여잡은 채 쓰러진 것 행인이 목격,\n 119 신고로 이송됨 이송 중에 의식 깨어 현재는 alert하나 흉통(NRS>7) 계속 호소중임",
1, "2023-07-20 13:11:22", "환자 본인", "- 보호자 대기(-) / 연락(+)\n- Chest Pain NRS 6점 -> noti(+) /처방(-)\n- ECG: ST Elevation r/o ischemic HF");

INSERT INTO tb_medical_order (
    "patient_register_id",
    "saved_timestamp",
    "order_statement",
    "recoder_doctor_id"
) values
(486124, "2023-07-18 02:23:44", "1. check v/s q 1hr", 1),
(486124, "2023-07-18 02:23:44", "2. restrict ABR", 1),
(486124, "2023-07-18 02:23:44", "3. Total NPO", 1),
(486124, "2023-07-18 02:23:44", "4. f/u BST q 6hr", 1),
(486124, "2023-07-18 02:23:44", "", 1),
(486124, "2023-07-18 02:23:44", "====== 수액 ========", 1),
(486124, "2023-07-18 02:23:44", "1. NS 1L/bag   100ml/hr", 1),
(486124, "2023-07-18 02:23:44", "", 1),
(486124, "2023-07-18 02:23:44", "====== PO ========", 1),
(486124, "2023-07-18 02:23:44", "1. Clopidrogel 300mg  6Tab", 1),
(486124, "2023-07-18 02:23:44", "2. Tigagreller 180mg 1Tab 둘 다 지금 복용해주세요", 1),
(486124, "2023-07-18 02:23:44", "", 1),
(486124, "2023-07-18 02:23:44", "====== Text Order =========", 1),
(486124, "2023-07-18 02:23:44", "보호자 대기 시켜주세요", 1),
(486124, "2023-07-18 02:23:44", "", 1),
(486124, "2023-07-18 02:23:44", "===== PCI Order ===========", 1),
(486124, "2023-07-18 02:23:44", "....", 1);