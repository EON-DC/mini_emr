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
	"allocated_bed_location_id"	INTEGER,
	"register_number"	INTEGER UNIQUE,
	FOREIGN KEY("allocated_bed_location_id") REFERENCES "tb_bed_of_ward"("bed_id"),
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

INSERT INTO tb_patient("birth_date", "name","sex", "ssn", "address", "type_insurance", "allocated_bed_location_id", "register_number") VALUES
('1958-06-08', '김철수', 'M', '580608-1354644', '경기도 수원시 언저리 어딘가', '건강보험', 1, 486124);

INSERT INTO tb_emergency_nurse_record(
    "onset_time",
    "register_id",
    "ktas_id",
    "cheif_complain",
    "description",
    "recorder_nurse_id",
    "saved_time",
    "responser") values
('1958-06-08',486124, 'AICAB', '가슴이 답답해요',
"내원전 2시간 전, 속 울렁거림, 가슴 답답함 느껴졌으나 시간 지나니 괜찮아짐, 식사 후 집으로 귀가하던 중 가슴 부여잡은 채 쓰러진 것 행인이 목격, 119 신고로 이송됨 이송 중에 의식 깨어 현재는 alert하나 흉통(NRS>7) 계속 호소중임",
1, "2023-07-20 13:11:22", "환자 본인");
