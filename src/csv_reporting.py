from src.reporting import reporting
class CSVReporting(reporting):


    def create(self, key: str) -> str:
        # Вот ваша логика для получения данных на основе ключа
        # Построить строку формата CSV на основе полученных данных
        # В демонстрационных целях предположим, что мы просто возвращаем фиктивную строку CSV
        csv_data = "data1,data2,data3\n"
        return csv_data