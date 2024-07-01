from datetime import datetime
from docxtpl import DocxTemplate


def render_template(template_path, context, output_path):
    # Открываем шаблон
    doc = DocxTemplate(template_path)

    # Рендерим шаблон с контекстом
    doc.render(context)

    # Сохраняем новый документ
    doc.save(output_path)


def main():
    # Данные для замены
    current_date = datetime.now()
    context = {
        "currentDate": {
            "day": current_date.day,
            "month": current_date.strftime('%B'),
            "year": current_date.year
        },
        "studentList": [
            {"name": "Иван", "surname": "Иванов", "familyname": "Иванович"},
            {"name": "Петр", "surname": "Петров", "familyname": "Петрович"}
        ]
    }

    template_path = 'D:/work/qoollo/TemplateFiller/Test/template.docx'
    output_path = 'D:/work/qoollo/TemplateFiller/Test/output.docx'
    render_template(template_path, context, output_path)

    print("Документ успешно обработан и сохранен.")


if __name__ == "__main__":
    main()
