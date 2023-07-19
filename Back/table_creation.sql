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
	PRIMARY KEY("ktas_id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS tb_department;
CREATE TABLE "tb_department" (
    "department_id"	INTEGER,
    "name"	INTEGER NOT NULL,
    PRIMARY KEY("department_id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS tb_doctor;
CREATE TABLE "tb_doctor" (
	"doctor_id"	INTEGER,
	"employee_id"	INTEGER NOT NULL,
	"assigned_department_id"	INTEGER NOT NULL,
	PRIMARY KEY("doctor_id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS tb_employee;
CREATE TABLE "tb_employee" (
	"employee_id"	INTEGER,
	"name"	TEXT NOT NULL,
	"type_job"	TEXT NOT NULL,
	"login_username"	TEXT NOT NULL UNIQUE,
	"login_password"	TEXT NOT NULL,
	"mobile_phone_num_1"	TEXT,
	"mobile_phone_num_2"	TEXT,
	PRIMARY KEY("employee_id" AUTOINCREMENT)
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
    "assgined_ward_id"	INTEGER NOT NULL,
    "additional_info"	TEXT,
    "viewing_bed_name"	TEXT NOT NULL,
    PRIMARY KEY("bed_id" AUTOINCREMENT),
    FOREIGN KEY("assgined_ward_id") REFERENCES "tb_department"
);

DROP TABLE IF EXISTS tb_emergency_nurse_record;
CREATE TABLE "tb_emergency_nurse_record" (
	"enr_id"	INTEGER,
	"onset_time"	TEXT,
	"ktas_id"	INTEGER,
	"cheif_complain"	TEXT,
	"description"	TEXT,
	"recorder_nurse_id"	INTEGER,
	"saved_time"	TEXT,
	PRIMARY KEY("enr_id" AUTOINCREMENT),
	FOREIGN KEY("recorder_nurse_id") REFERENCES "tb_nurse"("nurse_id")
);


DROP TABLE IF EXISTS tb_nurse;
CREATE TABLE "tb_nurse" (
	"nurse_id"	INTEGER,
	"employee_id"	INTEGER NOT NULL,
	"assigned_ward"	INTEGER NOT NULL,
	PRIMARY KEY("nurse_id" AUTOINCREMENT),
	FOREIGN KEY("employee_id") REFERENCES "tb_employee"("employee_id")
);

DROP TABLE IF EXISTS tb_administration;
CREATE TABLE "tb_administration" (
    "administration_id"	INTEGER,
    "employee_id"	INTEGER NOT NULL,
    "assigned_part"	INTEGER NOT NULL,
    PRIMARY KEY("administration_id" AUTOINCREMENT),
    FOREIGN KEY("employee_id") REFERENCES "tb_employee"("employee_id"),
    FOREIGN KEY("assigned_part") REFERENCES "tb_department"("department_id")
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

