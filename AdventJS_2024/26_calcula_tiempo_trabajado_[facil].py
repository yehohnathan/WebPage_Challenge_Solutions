"""
¡Santa Claus ya ha repartido todos los regalos! Ahora está revisando los
informes de productividad de los elfos. Pero hay un problema: la Product Owner,
Mrs. Claus 🧑‍🎄✨, necesita entender rápidamente si los elfos cumplieron con los
tiempos estimados. Están haciendo Agile Scream.

Para ayudar a Mrs. Claus, tu tarea es calcular el porcentaje completado de cada
tarea y devolverlo redondeado al número entero más cercano. Esto le permitirá
planificar mejor para la próxima Navidad y mantener a todos contentos.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def get_completed(time_worked: str, total_time: str) -> str:
    def to_seconds(hms: str) -> int:
        # Separa y convierte directamentente la hora, minutos y segundos
        h, m, s = map(int, hms.split(':'))
        return h * 3600 + m * 60 + s
    # Segundos trabajados y segundos totales
    worked_seconds = to_seconds(time_worked)
    total_seconds = to_seconds(total_time)
    # Porcentaje trabajado
    percent = round(worked_seconds / total_seconds * 100)
    return f'{percent}%'


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    print(get_completed('01:00:00', '03:00:00'))    # 33%
    print(get_completed('02:00:00', '04:00:00'))    # 50%
    print(get_completed('01:00:00', '01:00:00'))    # 100%
    print(get_completed('00:10:00', '01:00:00'))    # 17%
    print(get_completed('01:10:10', '03:30:30'))    # 33%
    print(get_completed('03:30:30', '05:50:50'))    # 60%


if __name__ == "__main__":
    main()
