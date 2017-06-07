from agingonehundredyearsui import AgingOneHundredYearsUI


def calc_future_year(current_year, target_age, actual_age):
    delta = target_age - actual_age
    return current_year + delta


def get_year_when_user_is_100(age):
    return calc_future_year(2016, 100, age)


if __name__ == "__main__":
    ui = AgingOneHundredYearsUI()
    ui.prompt_name()
    ui.prompt_age()
    ui.output_results(get_year_when_user_is_100(ui.age))
