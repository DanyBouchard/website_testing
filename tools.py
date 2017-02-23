import plotly

def chart(no_gender, male, female, apache_helicopter, tardigrade):
	""""Return a pie chart of the genre distribution on the board"""
	
	#offline plot
	fig = {
		"data": [
			{
				"labels": ["None", "Male", "Female", "Apache Helicopter", "Tardigrade"],
				"hoverinfo": "none",
				"marker": {
					"colors": [
						"rgb(0,255,0)",
						"rgb(255,0,0)",
						"rgb(0,0,255)",
						"rgb(0,255,255)",
						"rgb(255,255,255)"
					]
				},
				"type": "pie",
				"values": [no_gender, male, female, apache_helicopter, tardigrade]
			}
		],
		"layout":{
			"showlegend": True
			}
	}
	return plotly.offline.plot(fig, output_type="div", show_link=False, link_text=False)