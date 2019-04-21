def font_color(score):
    color = "green"
    try:
        if float(score) >= 0.56:
            color = "red"
    except:
        pass
    return color


if not results.analysis_report_status:
    noteText = u"""Successful submit <b>{}</b> to SNDBOX Platform. However it will take time to generate an analysis report, please submit it again later. <br>""".format(
        artifact.value)

else:
    noteText = u"""Successful submit <b>{}</b> to SNDBOX Platform. Check the results below: <br>""".format(
        artifact.value)

    for sample in results.sample_final_result:
        noteText += u"""-----------------------------------------------------------------------"""
        color = font_color(sample["sample_report"]["score"])
        noteText += u"""<br>SNDBOX Sandbox Analysis: <b>{sample_filename}</b> complete.<br>
                   SNDBOX Online Attachment: <a href={sample_online_report}>{sample_online_report}</a><br>
                   SNDBOX Analyzer result:  Score: <b style= "color:{color}">{sample_score}</b> <br>
               """.format(sample_filename=sample["sample_report"]["name"],
                          sample_online_report=sample["sample_report"]["sample_url"],
                          color=color,
                          sample_score=sample["sample_report"]["score"])

incident.addNote(helper.createRichText(noteText))
