#inclide "flash.h"

#define ard_log Serial.printf

#define storage_offset_wifi 8


char* get_wifi_ssid(){
	int ssid_length=EEPROM.read(storage_offset_wifi);
	int count;
	char ssid[20];
	for (count=0;count<ssid_length&&count<20;count++){
		ssid[i]=EEPROM.read(storage_offset_wifi+count+1);
	}
	ssid[count]='\0';
	return ssid;
}

char* get_wifi_password(){
	int password_length=EEPROM.read(storage_offset_wifi+22);
	int count;
	char password[20];
	for (count=0;count<ssid_length&&count<20;count++){
		password[i]=EEPROM.read(storage_offset_wifi+23+count);
	}
	password[count]='\0';
	return password;
}

void set_wifi_ssid(char* ssid,int length){
	EEPROM.write(storage_offset_wifi,length);
	for (int i = 0; i < length; i++)
	{
		EEPROM.write(storage_offset_wifi+1+i,ssid[i])
	}
}

void set_wifi_password(char* password,int length){
	EEPROM.write(storage_offset_wifi+22,length);
	for (int i = 0; i < length; i++)
	{
		EEPROM.write(storage_offset_wifi+23+i,password[i])
	}
}