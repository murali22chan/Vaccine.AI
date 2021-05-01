import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go

from tensoflow.keras.models import load_model

st.set_page_config(page_title="Vaccine.AI", page_icon="icon.png")
status=st.sidebar.radio('',('Home',"Safety Measures"))

if status =="Home":
	st.image("icon.png")
	st.markdown("# Vaccine.AI")

	age = st.number_input("Enter Your Age")
	sex = st.selectbox("Select Your Sex", ('Male','Female'))
	symptoms = st.multiselect("Choose All The Previous Health Conditions",('None','Hypertension', 'Asthma', 'Diabetes','Corona', 'Hypothyroidism', 'Hyperlipidemia', 'Chelestrol','Depression', 'Obesity', 'Kidney'))
	vaccine_name = st.selectbox("Select a Vaccine", ('PFIZER(BIONTECH)','MODERNA'))
	st.markdown("")

	if st.button('Predict Side Effects'):
		model = load_model('final2.h5', compile=False)
		x = []
		x.append(age)

		if sex == "Male":
			x.append(0)
		else:
			x.append(1)

		if vaccine_name == "PFIZER(BIONTECH)":
			x.append(0)
		else:
			x.append(1)

		if symptoms[0] == "None":
			for i in range(10):
				x.append(0)

		else:
			if "Hypertension" in symptoms:
				x.append(1)
			else:
				x.append(0)

			if "Asthma" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Diabetes" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Corona" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Hypothyroidism" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Hyperlipidemia" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Chelestrol" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Depression" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Obesity" in symptoms:
				x.append(1)
			else:
				x.append(0)
			if "Kidney" in symptoms:
				x.append(1)
			else:
				x.append(0)

		print(x)
		x = np.array(x)
		x = np.reshape(x, (1,13))
		y = model.predict(x)
		print(y)

		symptoms_label = ['BodyPain', 'Pyrexia', 'Headache', 'Dyspnoea', 'Fatigue', 'Chills','Dizziness', 'Nausea', 'Asthenia', 'Cough']
		indices = (-y).argsort()[:4]
		values = []
		labels = []
		for count in range(4):
			idx = np.where(indices==count)
			values.append(y[0][idx[1][0]])
			labels.append(symptoms_label[idx[1][0]])

		st.markdown("## Side Effects Likely to Get")
		fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
		st.plotly_chart(fig)

		st.markdown("")
		st.markdown("## Probality of Each Side Effects to Occur")
		fig2 = go.Figure([go.Bar(x=symptoms_label, y=y[0])])
		st.plotly_chart(fig2)


if status == "Safety Measures":
	st.markdown("# Wear Mask , Stay at Home, Stay Safe")
	st.image("icon2.png")

