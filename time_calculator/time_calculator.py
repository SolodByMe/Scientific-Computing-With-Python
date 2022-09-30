def pasar_modulo(date):
    date=date.split(" ")
    hour=date[0].split(":")[0]
    minutes=date[0].split(":")[1]
    time=date[1]
    extra_hours=0
    minute_s=int(minutes)
    contador_dias=0
    if(minute_s>=60):
        extra_hours=minute_s//60
        minutes=minute_s%60
        hour=int(hour)
        hour=hour+extra_hours
        hour=str(hour)
        minutes=str(minutes)
    hour_s=int(hour)
    if(hour_s>=12):
        hour=int(hour)
        cociente=hour//12
        while(cociente>0):
            if(time=="AM"):
                time="PM"
            elif(time=="PM"):
                time="AM"
                contador_dias+=1
            cociente-=1
        hour=str(hour%12)
    minute_s=int(minutes)
    if(minute_s<10):
        minutes="0"+str(minutes)
    if(contador_dias==0):
        return(hour+":"+minutes+ " "+time)
    elif(contador_dias==1):
        return(hour+":"+minutes+ " "+time+" (next day)")
    elif(contador_dias>1):
        return(hour+":"+minutes+ " "+time+" ("+str(contador_dias)+" days later)")
    return(hour+":"+minutes+ " "+time)

def añadir_tiempo(date,suma):
    hora_minuto=date.split(" ")[0]
    hora=hora_minuto.split(":")[0]
    minutos=hora_minuto.split(":")[1]
    hora_suma=suma.split(":")[0]
    minuto_suma=suma.split(":")[1]
    hora_final=str(int(hora)+int(hora_suma))
    minuto_final=str(int(minutos)+int(minuto_suma))
    return(hora_final+":"+minuto_final+" "+date.split(" ")[1])

def calculadora_tiempo(date,suma):
    check_time(suma)
    fecha_final=añadir_tiempo(date,suma)
    print(pasar_modulo(fecha_final))

def check_time(date):
    if(int(date.split(":")[1])>=60):
        raise ValueError("Los minutos deben ser menores que 60")
calculadora_tiempo("11:43 PM","24:20")