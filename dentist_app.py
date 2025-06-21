import streamlit as st
from PIL import Image
import webbrowser

# Set page config
st.set_page_config(page_title="Dentist Prognosis App", layout="wide")

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "home"
if 'current_symptom' not in st.session_state:
    st.session_state.current_symptom = None
if 'telugu_home' not in st.session_state:
    st.session_state.telugu_home = False
if 'telugu_education' not in st.session_state:
    st.session_state.telugu_education = False
# CSS Styles
st.markdown("""
<style>
    /* Force light theme colors */
    :root {
        --primary-color: #1A3F64;
        --background-color: #FFFFFF;
        --secondary-background-color: #F0F2F6;
        --text-color: #262730;
        --font: sans serif;
    }
    
    /* Main background */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* Uniform card styling */
    .uniform-card {
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(1, 47, 92, 0.1);
        padding: 16px;
        margin-bottom: 20px;
        background-color: white;
        transition: transform 0.2s;
        height: 100%;
        border: 1px solid #e0e0e0;
    }
    .uniform-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(1, 47, 92, 0.15);
    }
    .uniform-card img {
        border-radius: 6px;
        object-fit: cover;
        width: 100%;
        height: 200px;
        margin-bottom: 12px;
    }
    .uniform-card h4 {
        color: #012F5C;
        margin-top: 0;
        font-weight: 600;
    }
    .uniform-card p {
        color: #425973;
    }

    /* Info boxes */
    .info-box {
        background-color: white;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-left: 4px solid #1A3F64;
    }
    .warning-box {
        background-color: white;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-left: 4px solid #FFA500;
    }
    .success-box {
        background-color: white;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-left: 4px solid #4CAF50;
    }
    .error-box {
        background-color: white;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-left: 4px solid #F44336;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #012F5C !important;
    }
    .sidebar-button {
        width: 100%;
        margin-bottom: 8px;
        background-color: #1A3F64 !important;
        color: white !important;
        border: none !important;
        transition: all 0.3s ease;
    }
    .sidebar-button:hover {
        background-color: #425973 !important;
        transform: translateX(5px);
    }
    
    /* Titles */
    h1 {
        color: #012F5C !important;
        padding-bottom: 8px;
        border-bottom: 2px solid #1A3F64;
    }
    h2 {
        color: #1A3F64 !important;
    }
    h3 {
        color: #425973 !important;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #1A3F64;
        color: white;
        border: none;
        border-radius: 4px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #425973;
        transform: scale(1.02);
    }
    
    /* Button container */
    .button-container {
        display: flex;
        gap: 8px;
        margin-top: 12px;
    }
    .button-container button {
        flex: 1;
        border-radius: 4px;
    }
    
    /* Language toggle */
    .language-toggle {
        position: absolute;
        top: 10px;
        right: 10px;
        z-index: 1000;
        background-color: white;
        padding: 5px 10px;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Tabs styling */
    [data-baseweb="tab-list"] {
        gap: 10px;
    }
    [data-baseweb="tab"] {
        background-color: #F0F2F6 !important;
        border-radius: 4px !important;
        padding: 8px 16px !important;
        margin: 0 5px !important;
        transition: all 0.3s ease !important;
    }
    [data-baseweb="tab"]:hover {
        background-color: #E0E5EC !important;
    }
    [data-baseweb="tab"][aria-selected="true"] {
        background-color: #1A3F64 !important;
        color: white !important;
    }
    
    /* Input fields */
    .stTextInput>div>div>input, 
    .stTextArea>div>div>textarea, 
    .stNumberInput>div>div>input {
        border: 1px solid #e0e0e0 !important;
        border-radius: 4px !important;
    }
    
    /* Divider styling */
    hr {
        margin: 20px 0;
        border: none;
        height: 1px;
        background-color: #e0e0e0;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    ::-webkit-scrollbar-thumb {
        background: #1A3F64;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #012F5C;
    }
</style>
""", unsafe_allow_html=True)

# Symptoms Data
symptoms_data = {
    "Dental Caries(Early)": {
        "image": "images/dentist/Dental caries(Early).jpeg",
        "Symptom": "Pain",
        "duration": "<1 week",
        "probable condition": "Dental Caries (Early)",
        "advice": "Avoid sweets, maintain hygiene",
        "referral": "General Dentist",
        "learn more": "https://my.clevelandclinic.org/health/diseases/10946-cavities",
        "audio": "images/dentist/Dental Caries.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Avoid eating until numbness wears off.\n• Avoid chewing on the treated side for 24 hours if temporary filling placed.",
                "Telugu": "• నొప్పి నివారించే వరకు తినకుండా ఉండండి.\n• తాత్కాలిక ఫిల్లింగ్ వేసినట్లయితే 24 గంటల పాటు చికిత్స చేయబడిన పక్కవైపు నమిలకుండా ఉండండి."
            },
            "Medications": {
                "English": "• Mild pain: Paracetamol 500–650 mg every 6 hours as needed.\n• If allergic to Paracetamol: Ibuprofen 400 mg every 6–8 hours (if no gastric issues).\n• If allergic to NSAIDs: Use Acetaminophen only under medical supervision.",
                "Telugu": "• తేలికపాటి నొప్పికి: ప్రతి 6 గంటలకు అవసరమైనంత వరకు పారాసిటమాల్ 500–650 mg.\n• పారాసిటమాల్‌కు అలర్జీ ఉంటే: ఐబుప్రోఫెన్ 400 mg ప్రతి 6–8 గంటలకు (గ్యాస్ట్రిక్ సమస్యలు లేకపోతే మాత్రమే).\n• NSAIDs‌కు అలర్జీ ఉంటే: వైద్య పర్యవేక్షణలో మాత్రమే అసెటామినోఫెన్ వాడాలి."
            },
            "Diet & Lifestyle": {
                "English": "• Limit sugary and sticky foods.\n• Increase water intake.",
                "Telugu": "• తీపి మరియు అంటుకునే ఆహారాన్ని తగ్గించండి.\n• నీటి వినియోగాన్ని పెంచండి."
            },
            "Oral Hygiene": {
                "English": "• Brush with fluoride toothpaste twice daily.\n• Floss gently without touching the filling area.",
                "Telugu": "• ఫ్లోరైడ్ టూత్‌పేస్ట్‌తో రోజుకు రెండు సార్లు బ్రష్ చేయండి.\n• ఫిల్లింగ్ ఉన్న ప్రదేశాన్ని ముట్టకుండా మృదువుగా ఫ్లాస్ చేయండి."
            },
            "Follow-Up": {
                "English": "• 6-month dental check-up.\n• Sealants may be advised.",
                "Telugu": "• ప్రతి 6 నెలలకు ఒకసారి దంత వైద్యుడిని కలవాలి.\n• అవసరమైతే సీలెంట్లు సిఫారసు చేయబడవచ్చు."
            },
            "Seek Immediate Help If": {
                "English": "• Pain persists more than 48 hours.\n• Swelling or allergic rash develops.",
                "Telugu": "• నొప్పి 48 గంటలకుపైగా కొనసాగితే.\n• వాపు లేదా అలర్జీ సంబంధిత చర్మ రేఖలు ఏర్పడితే."
            }
        },
        "telugu": {
            "name": "ప్రారంభ దంత కాయిలు",
            "Symptom": "నొప్పి",
            "duration": "1 వారం కంటే తక్కువ",
            "probable condition": "ప్రారంభ దంత కాయిలు",
            "advice": "మిఠాయిలు తగ్గించండి, పరిశుభ్రతను పాటించండి",
            "referral": "సాధారణ దంత వైద్యుడు"
        }
    },
    "Dental Abscess": {
        "image": "images/dentist/Dental Abcess.jpg",
        "Symptom": "Pain",
        "duration": ">2 weeks",
        "probable condition": "Dental Abscess",
        "advice": "Salt rinse, visit dentist urgently",
        "referral": "Endodontists",
        "learn more": "https://my.clevelandclinic.org/health/diseases/10943-abscessed-tooth",
        "audio": "audio/dental_abscess.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Rinse gently with warm saline 3–4 times/day.\n• Avoid pressing or touching swollen area.",
                "Telugu": "• రోజు 3–4 సార్లు కోడి గోరింటాకు ఉప్పు నీటితో మృదువుగా పుక్కిలించండి.\n• వాపు ఉన్న ప్రదేశాన్ని ఒత్తకుండా లేదా ముట్టకుండా ఉండండి."
            },
            "Medications": {
                "English": "• Antibiotics: Amoxicillin 500 mg TID for 5–7 days.\n• If penicillin-allergic: Azithromycin 500 mg OD x 3 days or Clindamycin 300 mg TID.\n• Pain relief: Ibuprofen 400 mg TID or Paracetamol.\n• If NSAID-allergic: Paracetamol or Acetaminophen.",
                "Telugu": "• యాంటిబయోటిక్స్: అమోక్సిసిలిన్ 500 mg రోజుకు మూడు సార్లు 5–7 రోజులు.\n• పెనిసిలిన్‌కు అలర్జీ ఉంటే: ఆజిథ్రోమైసిన్ 500 mg రోజుకు ఒక్కసారి 3 రోజులు లేదా క్లిండమైసిన్ 300 mg రోజుకు మూడు సార్లు.\n• నొప్పికి: ఐబుప్రోఫెన్ 400 mg రోజుకు మూడు సార్లు లేదా పారాసిటమాల్.\n• NSAIDs కు అలర్జీ ఉంటే: పారాసిటమాల్ లేదా అసెటామినోఫెన్."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid cold and hot extremes.",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• గట్టి మరియు చల్లటి లేదా వేడిగా ఉన్న ఆహారాలు నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Do not brush on the abscess site.\n• Chlorhexidine 0.2% rinse twice daily.",
                "Telugu": "• పొప్పుడు ఉన్న ప్రదేశంలో బ్రష్ చేయవద్దు.\n• రోజుకు రెండు సార్లు 0.2% క్లోర్‌హెక్సిడిన్ మూతి ద్రావణం వాడండి."
            },
            "Follow-Up": {
                "English": "• 3–5 day review.\n• Root canal or extraction may be needed.",
                "Telugu": "• 3–5 రోజుల్లో మళ్లీ పరీక్ష.\n• రూట్ కెనాల్ లేదా పళ్ల తొలగింపు అవసరమవుతుందో తెలుసుకోండి."
            },
            "Seek Immediate Help If": {
                "English": "• Swelling spreads to neck or eye.\n• Fever >101°F or breathing difficulty.",
                "Telugu": "• వాపు మెడ లేదా కంటి వరకు వ్యాపిస్తే.\n• జ్వరం 101°F కంటే ఎక్కువ అయితే లేదా శ్వాస తీసుకోవడంలో ఇబ్బంది ఉంటే."
            }
        },
        "telugu": {
            "name": "దంత పొప్పుడు",
            "Symptom": "నొప్పి",
            "duration": "2 వారాలు కంటే ఎక్కువ",
            "probable condition": "దంత పొప్పుడు",
            "advice": "ఉప్పు నీటితో పుక్కిలించండి, త్వరగా డెంటిస్ట్ను సంప్రదించండి",
            "referral": "ఎండోడోంటిస్ట్"
        }
    },
    "Periapical Abscess": {
        "image": "images/dentist/Periapical Abscess.jpg",
        "Symptom": "Pain + Swelling",
        "duration": "Any",
        "probable condition": "Periapical Abscess",
        "advice": "Warm saline rinse, analgesics",
        "referral": "Endodontist",
        "learn more": "https://my.clevelandclinic.org/health/diseases/24896-periapical-abscess",
        "audio": "audio/periapical_abscess.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడు సూచించిన యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉన్నవారికి ప్రత్యామ్నాయాలు: ఆజిథ్రోమైసిన్, పారాసిటమాల్."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• వేడి, మసాలా, గట్టి ఆహారాలు నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ రిన్స్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటిస్టు రివ్యూ చేయించండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి/వాపు పెరిగితే.\n• అధిక జ్వరం లేదా ఇన్ఫెక్షన్ వ్యాపిస్తే."
            }
        },
        "telugu": {
            "name": "పీరియాపికల్ పొప్పుడు",
            "Symptom": "నొప్పి + వాపు",
            "duration": "ఏదైనా",
            "probable condition": "పీరియాపికల్ పొప్పుడు",
            "advice": "వేడి ఉప్పు నీటితో పుక్కిలించండి, నొప్పి నివారకాలు తీసుకోండి",
            "referral": "ఎండోడోంటిస్ట్"
        }
    },
    "Gingivitis": {
        "image": "images/dentist/Gingivitis.jpeg",
        "Symptom": "Bleeding Gums",
        "duration": "Any",
        "probable condition": "Gingivitis",
        "advice": "Brush twice daily, floss, chlorhexidine rinse",
        "referral": "Periodontist",
        "learn more": "https://my.clevelandclinic.org/health/diseases/10950-gingivitis-and-periodontal-disease-gum-disease",
        "audio": "audio/gingivitis.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Some bleeding after cleaning is normal.\n• Warm saline rinse for 2–3 days.",
                "Telugu": "• క్లీనింగ్ తర్వాత కొద్దిగా రక్తస్రావం సాధారణం.\n• 2–3 రోజులు గోరింటాకు ఉప్పు నీటితో పుక్కిలించండి."
            },
            "Medications": {
                "English": "• Chlorhexidine 0.2% rinse twice daily.\n• Multivitamin if advised.",
                "Telugu": "• క్లోర్‌హెక్సిడిన్ 0.2% మూతి ద్రావణం రోజుకు రెండు సార్లు.\n• అవసరమైతే మల్టీవిటమిన్."
            },
            "Diet & Lifestyle": {
                "English": "• Increase intake of green leafy vegetables and citrus.\n• Quit smoking.",
                "Telugu": "• ఆకుకూరలు మరియు సిట్రస్ పండ్ల వినియోగాన్ని పెంచండి.\n• పొగతాగే అలవాటును మానేయండి."
            },
            "Oral Hygiene": {
                "English": "• Brush with soft toothbrush.\n• Floss carefully daily.",
                "Telugu": "• మృదువైన బ్రష్ వాడండి.\n• రోజూ జాగ్రత్తగా ఫ్లాస్ చేయండి."
            },
            "Follow-Up": {
                "English": "• Reassess after 2–3 weeks.\n• Professional cleaning every 6 months.",
                "Telugu": "• 2–3 వారాల తర్వాత మళ్లీ పరీక్షించాలి.\n• ప్రతి 6 నెలలకు ప్రొఫెషనల్ క్లీనింగ్ చేయించాలి."
            },
            "Seek Immediate Help If": {
                "English": "• Bleeding doesn't stop or increases.",
                "Telugu": "• రక్తస్రావం ఆగకపోతే లేదా పెరుగుతుంటే."
            }
        },
        "telugu": {
            "name": "జింజివైటిస్",
            "Symptom": "చిగుళ్ళ నుండి రక్తస్రావం",
            "duration": "ఏదైనా",
            "probable condition": "జింజివైటిస్",
            "advice": "రోజుకు రెండుసార్లు బ్రష్ చేయండి, ఫ్లాస్ చేయండి, క్లోర్‌హెక్సిడిన్ రిన్స్ వాడండి",
            "referral": "పీరియోడోంటిస్ట్"
        }
    },
    "Periodontitis": {
        "image": "images/dentist/Periodontitis.jpeg",
        "Symptom": "Bleeding + Swollen Gums",
        "duration": ">2 weeks",
        "probable condition": "Periodontitis",
        "advice": "Scaling needed, professional cleaning",
        "referral": "Periodontist",
        "learn more": "https://my.clevelandclinic.org/health/diseases/16620-periodontitis",
        "audio": "audio/periodontitis.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడు సూచించిన యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉన్నవారికి ప్రత్యామ్నాయాలు: ఆజిథ్రోమైసిన్, పారాసిటమాల్."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• వేడి, మసాలా, గట్టి ఆహారాలు నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటిస్టు వద్ద రివ్యూకు వెళ్లండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు పెరిగితే.\n• ఎక్కువ జ్వరం లేదా ఇన్ఫెక్షన్ వ్యాప్తిస్తే."
            }
        },
        "telugu": {
            "name": "పిరియోడొంటిటిస్",
            "Symptom": "చిగుళ్ళ నుండి రక్తస్రావం + వాపు",
            "duration": "2 వారాలు కంటే ఎక్కువ",
            "probable condition": "పిరియోడొంటిటిస్",
            "advice": "స్కేలింగ్ అవసరం, ప్రొఫెషనల్ క్లీనింగ్",
            "referral": "పీరియోడోంటిస్ట్"
        }
    },
    "Halitosis": {
        "image": "images/dentist/Halitosis.jpg",
        "Symptom": "Bad Breath",
        "duration": ">1 week",
        "probable condition": "Halitosis / Periodontal Issue",
        "advice": "Mouthwash, tongue cleaning, hydration",
        "referral": "Periodontist",
        "learn more": "https://my.clevelandclinic.org/health/diseases/17771-bad-breath-halitosis",
        "audio": "audio/halitosis.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడు సూచించిన యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉన్నవారికి ప్రత్యామ్నాయాలు: ఆజిథ్రోమైసిన్, పారాసిటమాల్."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• వేడి, మసాలా, గట్టి పదార్థాలు నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటల్ రివ్యూ చేయించండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి/వాపు పెరిగితే.\n• అధిక జ్వరం లేదా వ్యాప్తించే ఇన్ఫెక్షన్ ఉంటే."
            }
        },
        "telugu": {
            "name": "హాలిటోసిస్",
            "Symptom": "నోటి దుర్వాసన",
            "duration": "1 వారం కంటే ఎక్కువ",
            "probable condition": "హాలిటోసిస్ / పీరియోడోంటల్ సమస్య",
            "advice": "మౌత్ వాష్ వాడండి, నాలుక శుభ్రం చేయండి, నీరు ఎక్కువగా తాగండి",
            "referral": "పీరియోడోంటిస్ట్"
        }
    },
    "Trauma": {
        "image": "images/dentist/Trauma.jpg",
        "Symptom": "Loose Tooth",
        "duration": "Any",
        "probable condition": "Trauma / Advanced Periodontitis",
        "advice": "Avoid pressure, consult urgently",
        "referral": "Oral Surgeon",
        "learn more": "https://my.clevelandclinic.org/health/diseases/16916-dental-injuries",
        "audio": "audio/trauma_periodontitis.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Cold compress.\n• Avoid chewing on the side.\n• Use antiseptic rinse.",
                "Telugu": "• చల్లటి కాంప్రెస్ ఉపయోగించండి.\n• చికిత్స పక్కవైపు నమిలకండి.\n• యాంటీసెప్టిక్ మూతి ద్రావణం వాడండి."
            },
            "Medications": {
                "English": "• Pain relief: Diclofenac 50 mg BID or Ketorolac 10 mg QID.\n• If NSAID-allergic: Paracetamol or Tramadol (prescribed only).\n• Antibiotics: Amoxicillin-Clavulanate 625 mg TID.\n• If allergic: Metronidazole + Azithromycin/Clindamycin.\n• Rinse: Chlorhexidine 0.2%.",
                "Telugu": "• నొప్పికి: డైక్లోఫెనాక్ 50 mg రోజుకు రెండు సార్లు లేదా కీటోరోలాక్ 10 mg రోజుకు నాలుగు సార్లు.\n• NSAIDs కు అలర్జీ ఉంటే: పారాసిటమాల్ లేదా ట్రామడాల్ (వైద్యుని సలహాతో మాత్రమే).\n• యాంటిబయోటిక్స్: అమోక్సిసిలిన్-క్లావులనేట్ 625 mg రోజుకు మూడు సార్లు.\n• అలర్జీ ఉంటే: మెట్రోనిడజోల్ + ఆజిథ్రోమైసిన్ / క్లిండమైసిన్.\n• మౌఖిక క్లీన్ కోసం: క్లోర్‌హెక్సిడిన్ 0.2% మూతి ద్రావణం."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• వేడి, మసాలా, గట్టి పదార్థాలు నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడండి."
            },
            "Follow-Up": {
                "English": "• 3–5 days; may need splinting or extraction.",
                "Telugu": "• 3–5 రోజుల్లో పరీక్ష. అవసరమైతే స్ప్లింటింగ్ లేదా తొలగింపు."
            },
            "Seek Immediate Help If": {
                "English": "• Severe swelling or loosening of teeth.",
                "Telugu": "• తీవ్రమైన వాపు లేదా పళ్లు లూస్ అయిపోవడం."
            }
        },
        "telugu": {
            "name": "గాయం / అధిక పిరియోడొంటల్ వ్యాధి",
            "Symptom": "దంతం వదులుగా ఉండటం",
            "duration": "ఏదైనా",
            "probable condition": "గాయం / అధిక పిరియోడొంటల్ వ్యాధి",
            "advice": "ప్రెషర్ ను నివారించండి, తక్షణం సంప్రదించండి",
            "referral": "ఓరల్ సర్జన్"
        }
    },
    "Enamel Erosion": {
        "image": "images/dentist/Enamel Erosion.webp",
        "Symptom": "Sensitivity (cold/sweet)",
        "duration": "Any",
        "probable condition": "Enamel Erosion / Caries",
        "advice": "Use desensitizing toothpaste",
        "referral": "General Dentist",
        "learn more": "https://my.clevelandclinic.org/health/diseases/tooth-erosion",
        "audio": "audio/enamel_erosion.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడి సూచనల మేరకు యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉన్నవారికి ప్రత్యామ్నాయ ఔషధాలు: ఆజిథ్రోమైసిన్, పారాసిటమాల్."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• వేడి, మసాలా మరియు గట్టి ఆహారాలను నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటిస్ట్ రివ్యూ చేయించాలి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు పెరిగితే.\n• అధిక జ్వరం లేదా వ్యాప్తించే ఇన్ఫెక్షన్ ఉంటే."
            }
        },
        "telugu": {
            "name": "ఎనామెల్ తొలిక",
            "Symptom": "సున్నితత్వం (చల్లదనం/తీపి)",
            "duration": "ఏదైనా",
            "probable condition": "ఎనామెల్ తొలిక / కేరీస్",
            "advice": "సున్నితత్వం తగ్గించే టూత్‌పేస్ట్ వాడండి",
            "referral": "సాధారణ దంత వైద్యుడు"
        }
    },
    "Cracked Tooth Syndrome": {
        "image": "images/dentist/Cracked Tooth Syndrome.jpg",
        "Symptom": "Pain on Biting",
        "duration": "Any",
        "probable condition": "Cracked Tooth Syndrome",
        "advice": "Avoid chewing on affected side, dental visit required",
        "referral": "Endodontist",
        "learn more": "https://my.clevelandclinic.org/health/diseases/21628-fractured-tooth-cracked-tooth",
        "audio": "audio/cracked_tooth.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడు సూచించిన యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉంటే: ఆజిథ్రోమైసిన్, పారాసిటమాల్ వంటివి ఉపయోగించండి."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారాలు తీసుకోండి.\n• వేడి, మసాలా మరియు గట్టి పదార్థాలు నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ రిన్స్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటిస్టును కలవండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు అధికమైతే.\n• జ్వరం పెరిగితే లేదా ఇన్ఫెక్షన్ వ్యాపిస్తే."
            }
        },
        "telugu": {
            "name": "పగిలిన దంత లక్షణం",
            "Symptom": "కొరుకుతున్నప్పుడు నొప్పి",
            "duration": "ఏదైనా",
            "probable condition": "పగిలిన దంత లక్షణం",
            "advice": "ప్రభావిత వైపు నమలకండి, దంత వైద్యుడిని సంప్రదించండి",
            "referral": "ఎండోడోంటిస్ట్"
        }
    },
    "Traumatic Ulcer": {
        "image": "images/dentist/Traumatic Ulcer.jpg",
        "Symptom": "Ulcers in Mouth",
        "duration": "<2 weeks",
        "probable condition": "Traumatic Ulcer",
        "advice": "Avoid spicy food, apply topical gel",
        "referral": "Oral Medicine Specialist",
        "learn more": "https://my.clevelandclinic.org/health/diseases/21766-mouth-ulcer",
        "audio": "audio/traumatic_ulcer.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడి సూచించిన యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉన్నవారికి: ఆజిథ్రోమైసిన్ లేదా పారాసిటమాల్ వంటివి."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• వేడి, మసాలా మరియు గట్టి పదార్థాలు నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటల్ రివ్యూ చేయించండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు పెరిగితే.\n• అధిక జ్వరం లేదా వ్యాప్తించే ఇన్ఫెక్షన్ ఉంటే."
            }
        },
        "telugu": {
            "name": "గాయం వల్ల ఏర్పడే పుండ్లు",
            "Symptom": "నోటిలో పుండ్లు",
            "duration": "2 వారాలు కంటే తక్కువ",
            "probable condition": "గాయం వల్ల ఏర్పడే పుండ్లు",
            "advice": "మసాలా ఆహారం నివారించండి, టాపికల్ జెల్ వాడండి",
            "referral": "ఓరల్ మెడిసిన్ స్పెషలిస్ట్"
        }
    },
    "Aphthous / Malignancy Suspicion": {
        "image": "images/dentist/Apthous.jpg",
        "Symptom": "Ulcers in Mouth",
        "duration": ">2 weeks",
        "probable condition": "Aphthous / Malignancy Suspicion",
        "advice": "Consult urgently if non-healing",
        "referral": "Oral Medicine Specialist",
        "learn more": "https://my.clevelandclinic.org/health/diseases/21766-mouth-ulcer",
        "audio": "audio/aphthous.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడు సూచించిన యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉన్నవారికి ప్రత్యామ్నాయాలు: ఆజిథ్రోమైసిన్, పారాసిటమాల్."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• వేడి, మసాలా, గట్టి పదార్థాలు నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటిస్టును కలవండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు పెరిగితే.\n• అధిక జ్వరం లేదా వ్యాప్తించే ఇన్ఫెక్షన్ ఉంటే."
            }
        },
        "telugu": {
            "name": "ఆఫ్తస్ / క్యాన్సర్ అనుమానం",
            "Symptom": "నోటిలో పుండ్లు",
            "duration": "2 వారాలు కంటే ఎక్కువ",
            "probable condition": "ఆఫ్తస్ / క్యాన్సర్ అనుమానం",
            "advice": "సరిగ్గా నయం కానప్పుడు తక్షణం సంప్రదించండి",
            "referral": "ఓరల్ మెడిసిన్ స్పెషలిస్ట్"
        }
    },
    "Leukoplakia (Precancerous)": {
        "image": "images/dentist/Leukoplakia.jpg",
        "Symptom": "White patches in mouth",
        "duration": ">2 weeks",
        "probable condition": "Leukoplakia (Precancerous)",
        "advice": "Biopsy advised, avoid tobacco",
        "referral": "Oral Medicine Specialist",
        "learn more": "https://my.clevelandclinic.org/health/diseases/17655-leukoplakia",
        "audio": "audio/leukoplakia.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడి సూచనల మేరకు ఔషధాలు వాడండి.\n• అలర్జీ ఉన్నవారికి: ఆజిథ్రోమైసిన్, పారాసిటమాల్ వంటి ప్రత్యామ్నాయాలు."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• వేడి, మసాలా, గట్టి పదార్థాలు తినకండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటల్ రివ్యూ చేయించండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు పెరిగితే.\n• అధిక జ్వరం లేదా ఇన్ఫెక్షన్ వ్యాపిస్తే."
            }
        },
        "telugu": {
            "name": "ల్యూకోప్లేకియా (క్యాన్సర్ ముందు స్థితి)",
            "Symptom": "నోటిలో తెల్లటి మచ్చలు",
            "duration": "2 వారాలు కంటే ఎక్కువ",
            "probable condition": "ల్యూకోప్లేకియా (క్యాన్సర్ ముందు స్థితి)",
            "advice": "బయోప్సీ సిఫార్సు, పొగతాగడం నివారించండి",
            "referral": "ఓరల్ మెడిసిన్ స్పెషలిస్ట్"
        }
    },
    "Erythroplakia (High Risk)": {
        "image": "images/dentist/Erythroplakia.jpg",
        "Symptom": "Red Patch in Mouth",
        "duration": ">2 weeks",
        "probable condition": "Erythroplakia (High Risk)",
        "advice": "Refer for biopsy, tobacco cessation",
        "referral": "Oral Medicine Specialist",
        "learn more": "https://my.clevelandclinic.org/health/diseases/21766-mouth-ulcer",
        "audio": "audio/erythroplakia.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడు సూచించిన యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉంటే: ఆజిథ్రోమైసిన్, పారాసిటమాల్ వంటివి వాడండి."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారాన్ని మాత్రమే తీసుకోండి.\n• వేడి, మసాలా మరియు గట్టి పదార్థాలను తినకండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ రిన్స్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డాక్టర్ వద్ద ఫాలో అప్ చేయండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు పెరిగితే.\n• అధిక జ్వరం లేదా ఇన్ఫెక్షన్ వ్యాప్తిస్తే."
            }
        },
        "telugu": {
            "name": "ఎరిథ్రోప్లేకియా (అధిక ప్రమాదం)",
            "Symptom": "నోటిలో ఎర్రటి మచ్చ",
            "duration": "2 వారాలు కంటే ఎక్కువ",
            "probable condition": "ఎరిథ్రోప్లేకియా (అధిక ప్రమాదం)",
            "advice": "బయోప్సీకి రిఫర్ చేయండి, పొగతాగడం మానేయండి",
            "referral": "ఓరల్ మెడిసిన్ స్పెషలిస్ట్"
        }
    },
    "TMJ Dysfunction": {
        "image": "images/dentist/TMJ Dysfunction.jpeg",
        "Symptom": "Pain Near Jaw Joint (TMJ)",
        "duration": "Any",
        "probable condition": "TMJ Dysfunction",
        "advice": "Warm compress, soft food, stress relief",
        "referral": "Oral Surgeon",
        "learn more": "https://my.clevelandclinic.org/health/diseases/15066-temporomandibular-disorders-tmd-overview",
        "audio": "audio/tmj_dysfunction.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వైద్యుడి సూచన మేరకు వాడాలి.\n• అలర్జీ ఉంటే: ఆజిథ్రోమైసిన్, పారాసిటమాల్ వంటివి వాడండి."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• గట్టి, మసాలా, వేడి పదార్థాలు తినకండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయాలి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడాలి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటల్ రివ్యూ చేయించాలి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు పెరిగితే.\n• అధిక జ్వరం లేదా వ్యాప్తించే ఇన్ఫెక్షన్ ఉంటే."
            }
        },
        "telugu": {
            "name": "టీఎంజే డిస్‌ఫంక్షన్",
            "Symptom": "దవడ ఉమ్మడి స్థలం దగ్గర నొప్పి (TMJ)",
            "duration": "ఏదైనా",
            "probable condition": "టీఎంజే డిస్‌ఫంక్షన్",
            "advice": "వేడి కాంప్రెస్ వేయండి, మృదువైన ఆహారం తీసుకోండి, ఒత్తిడి తగ్గించండి",
            "referral": "ఓరల్ సర్జన్"
        }
    },
    "TMJ Internal Derangement": {
        "image": "images/dentist/TMJ Internal Derangement.jpeg",
        "Symptom": "Clicking Sound from TMJ",
        "duration": "Any",
        "probable condition": "TMJ Internal Derangement",
        "advice": "Avoid wide opening, soft food diet",
        "referral": "Oral Surgeon",
        "learn more": "https://www.msdmanuals.com/professional/dental-disorders/temporomandibular-disorders/internal-temporomandibular-joint-tmj-derangement#Key-Points_v42292182",
        "audio": "audio/tmj_derangement.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడు సూచించిన యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉన్నవారికి ప్రత్యామ్నాయాలు: ఆజిథ్రోమైసిన్, పారాసిటమాల్."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారాలు తీసుకోండి.\n• వేడి, మసాలా మరియు గట్టి పదార్థాలను నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డాక్టర్ వద్ద పునఃపరిశీలన చేయించండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు అధికమైతే.\n• అధిక జ్వరం లేదా వ్యాప్తించే ఇన్ఫెక్షన్ ఉంటే."
            }
        },
        "telugu": {
            "name": "టీఎంజే లోపభూయిష్టం",
            "Symptom": "టీఎంజే నుండి క్లిక్ చేసే శబ్దం",
            "duration": "ఏదైనా",
            "probable condition": "టీఎంజే లోపభూయిష్టం",
            "advice": "నోరు విశాలంగా తెరవడం నివారించండి, మృదువైన ఆహారం తీసుకోండి",
            "referral": "ఓరల్ సర్జన్"
        }
    },
    "Trismus / Infection": {
        "image": "images/dentist/Trismus.webp",
        "Symptom": "Difficulty opening mouth",
        "duration": "Acute onset",
        "probable condition": "Trismus / Infection",
        "advice": "Warm compress, urgent dental visit",
        "referral": "Oral Surgeon",
        "learn more": "https://my.clevelandclinic.org/health/diseases/24086-trismus",
        "audio": "audio/trismus.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడు సూచించిన యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉన్నవారికి ప్రత్యామ్నాయాలు: ఆజిథ్రోమైసిన్, పారాసిటమాల్."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• వేడి, మసాలా, గట్టి పదార్థాలు నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటిస్టు రివ్యూ చేయించండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు పెరిగితే.\n• అధిక జ్వరం లేదా ఇన్ఫెక్షన్ వ్యాపిస్తే."
            }
        },
        "telugu": {
            "name": "ట్రిస్మస్ / ఇన్ఫెక్షన్",
            "Symptom": "నోరు తెరవడంలో ఇబ్బంది",
            "duration": "అకస్మాత్తుగా",
            "probable condition": "ట్రిస్మస్ / ఇన్ఫెక్షన్",
            "advice": "వేడి కాంప్రెస్ వేయండి, తక్షణం దంత వైద్యుడిని సంప్రదించండి",
            "referral": "ఓరల్ సర్జన్"
        }
    },
    "Parotitis / Salivary Gland Issue": {
        "image": "images/dentist/Parotitis.jpg",
        "Symptom": "Swelling Near Cheek/Ear",
        "duration": "Any",
        "probable condition": "Parotitis / Salivary Gland Issue",
        "advice": "Stay hydrated, lemon candy, consult specialist",
        "referral": "Oral Surgeon",
        "learn more": "https://my.clevelandclinic.org/health/diseases/23577-parotitis-parotid-gland-swelling",
        "audio": "audio/parotitis.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడు సూచించిన యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉన్నవారికి ప్రత్యామ్నాయాలు: ఆజిథ్రోమైసిన్, పారాసిటమాల్."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• వేడి, మసాలా, గట్టి పదార్థాలు నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటిస్టు రివ్యూ చేయించండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు పెరిగితే.\n• అధిక జ్వరం లేదా ఇన్ఫెక్షన్ వ్యాపిస్తే."
            }
        },
        "telugu": {
            "name": "పారొటిటిస్ / లాలాజల గ్రంధి సమస్య",
            "Symptom": "కెంపు/చెవి దగ్గర వాపు",
            "duration": "ఏదైనా",
            "probable condition": "పారొటిటిస్ / లాలాజల గ్రంధి సమస్య",
            "advice": "నీటి త్రాగడం పెంచండి, నిమ్మకాయ మిఠాయి, స్పెషలిస్ట్‌ను సంప్రదించండి",
            "referral": "ఓరల్ సర్జన్"
        }
    },
    "Staining": {
        "image": "images/dentist/Staining.jpg",
        "Symptom": "Black Discoloration of Teeth",
        "duration": "Chronic",
        "probable condition": "Caries / Staining",
        "advice": "Oral prophylaxis, restorations",
        "referral": "General Dentist",
        "learn more": "https://my.clevelandclinic.org/health/symptoms/10958-tooth-discoloration",
        "audio": "audio/staining.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడు సూచించిన యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉన్నవారికి ప్రత్యామ్నాయాలు: ఆజిథ్రోమైసిన్, పారాసిటమాల్."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• వేడి, మసాలా, గట్టి పదార్థాలు నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటిస్టు రివ్యూ చేయించండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు పెరిగితే.\n• అధిక జ్వరం లేదా ఇన్ఫెక్షన్ వ్యాపిస్తే."
            }
        },
        "telugu": {
            "name": "మచ్చలు",
            "Symptom": "పళ్ళపై నల్లని మచ్చలు",
            "duration": "దీర్ఘకాలికం",
            "probable condition": "కేరీస్ / మచ్చలు",
            "advice": "ఓరల్ ప్రొఫైలాక్సిస్, పునరుద్ధరణలు",
            "referral": "సాధారణ దంత వైద్యుడు"
        }
    },
    "Dental Trauma": {
        "image": "images/dentist/Dental Trauma.jpeg",
        "Symptom": "Broken/Fractured Tooth",
        "duration": "Recent",
        "probable condition": "Dental Trauma",
        "advice": "Preserve fragment, immediate consult",
        "referral": "Endodontist / Pedodontist",
        "learn more": "https://www.mayoclinic.org/dental-emergencies",
        "audio": "audio/dental_trauma.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడు సూచించిన యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉన్నవారికి ప్రత్యామ్నాయాలు: ఆజిథ్రోమైసిన్, పారాసిటమాల్."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• వేడి, మసాలా, గట్టి పదార్థాలు నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటిస్టు రివ్యూ చేయించండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు పెరిగితే.\n• అధిక జ్వరం లేదా ఇన్ఫెక్షన్ వ్యాపిస్తే."
            }
        },
        "telugu": {
            "name": "దంత గాయం",
            "Symptom": "పగిలిన/ఉలిసిన పళ్ళు",
            "duration": "ఇటీవల",
            "probable condition": "దంత గాయం",
            "advice": "పగిలిన భాగాన్ని సంరక్షించండి, తక్షణం సంప్రదించండి",
            "referral": "ఎండోడోంటిస్ట్ / పీడోడోంటిస్ట్"
        }
    },
    "Pericoronitis (Wisdom Tooth)": {
        "image": "images/dentist/Pericoronitis (Wisdom Tooth).webp",
        "Symptom": "Tooth Eruption Pain",
        "duration": "In teens",
        "probable condition": "Pericoronitis (Wisdom Tooth)",
        "advice": "Warm saline rinse, painkillers, dental visit",
        "referral": "Oral Surgeon",
        "learn more": "https://my.clevelandclinic.org/health/diseases/24142-pericoronitis",
        "audio": "audio/pericoronitis.mp3",
        "post_treatment_care": {
            "Immediate Post-Treatment Care": {
                "English": "• Follow standard dental post-care measures.",
                "Telugu": "• సాధారణ దంత చికిత్స తర్వాత తీసుకునే జాగ్రత్తలు పాటించండి."
            },
            "Medications": {
                "English": "• Use prescribed antibiotics and painkillers.\n• Offer alternatives in case of allergies (e.g., Azithromycin, Paracetamol).",
                "Telugu": "• వైద్యుడు సూచించిన యాంటిబయోటిక్స్ మరియు నొప్పినివారకాలు వాడండి.\n• అలర్జీ ఉన్నవారికి ప్రత్యామ్నాయాలు: ఆజిథ్రోమైసిన్, పారాసిటమాల్."
            },
            "Diet & Lifestyle": {
                "English": "• Soft food diet.\n• Avoid triggers (hot, spicy, hard foods).",
                "Telugu": "• మృదువైన ఆహారం తీసుకోండి.\n• వేడి, మసాలా, గట్టి పదార్థాలు నివారించండి."
            },
            "Oral Hygiene": {
                "English": "• Soft brushing.\n• Antiseptic rinses as advised.",
                "Telugu": "• మృదువుగా బ్రష్ చేయండి.\n• యాంటీసెప్టిక్ మౌత్ వాష్ వాడండి."
            },
            "Follow-Up": {
                "English": "• Dentist review in 3–7 days.",
                "Telugu": "• 3–7 రోజుల్లో డెంటిస్ట్‌ను సంప్రదించండి."
            },
            "Seek Immediate Help If": {
                "English": "• Pain/swelling worsens.\n• High fever or spreading infection.",
                "Telugu": "• నొప్పి లేదా వాపు పెరిగితే.\n• అధిక జ్వరం లేదా ఇన్ఫెక్షన్ వ్యాపిస్తే."
            }
        },
        "telugu": {
            "name": "పెరికోరోనైటిస్ (జ్ఞాన దంతం)",
            "Symptom": "దంతం మొలకెత్తే సమయంలో నొప్పి",
            "duration": "టీనేజ్ వయస్సులో",
            "probable condition": "పెరికోరోనైటిస్ (జ్ఞాన దంతం)",
            "advice": "వేడి ఉప్పు నీటితో పుక్కిలించండి, నొప్పి నివారకాలు తీసుకోండి, డెంటిస్ట్‌ను సంప్రదించండి",
            "referral": "ఓరల్ సర్జన్"
        }
    }
}

# Initialize language toggles for all symptoms
for symptom_key in symptoms_data.keys():
    if f'telugu_{symptom_key}' not in st.session_state:
        st.session_state[f'telugu_{symptom_key}'] = False

# Image Handling Functions
@st.cache_data
def load_and_resize_image(image_path, target_width=300, target_height=200):
    """Load and resize image uniformly"""
    try:
        img = Image.open(image_path)
        ratio = min(target_width/img.width, target_height/img.height)
        new_size = (int(img.width * ratio), int(img.height * ratio))
        img = img.resize(new_size, Image.Resampling.LANCZOS)
        new_img = Image.new('RGB', (target_width, target_height), (245, 245, 245))
        new_img.paste(img, ((target_width - new_size[0]) // 2, 
                           (target_height - new_size[1]) // 2))
        return new_img
    except:
        return Image.new('RGB', (target_width, target_height), (220, 220, 220))

def image_to_base64(image):
    """Convert PIL image to base64 string"""
    import io
    import base64
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Sidebar Navigation
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <h1 style='color: white; font-size: 28px; margin-bottom: 5px;'>Symptodent</h1>
        <p style='color: #a8c7fa; font-size: 14px; margin-top: 0;'>Dental Health Companion</p>
    </div>
    """, unsafe_allow_html=True)
    
    nav_options = [
        {"label": "🏠 Home", "page": "home"},
        {"label": "🔍 Symptom Explorer", "page": "symptom_explorer"},
        {"label": "📚 Education", "page": "education"},
        {"label": "📝 Feedback", "page": "feedback"}
    ]
    
    for option in nav_options:
        if st.button(option["label"], 
                   key=f"sidebar_{option['page']}", 
                   use_container_width=True,
                   help=f"Go to {option['page'].replace('_', ' ')}"):
            st.session_state.page = option["page"]
            st.rerun()
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #a8c7fa; font-size: 12px; margin-top: 20px;'>
        Bridging gaps in oral health through digital innovation
    </div>
    """, unsafe_allow_html=True)

# Page Functions
def show_home():
    is_telugu_home = st.session_state.telugu_home
    
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title("సింప్టోడెంట్" if is_telugu_home else "Symptodent")
    with col2:
        if st.button("తెలుగులో చూడండి" if not is_telugu_home else "View in English", 
                    key="lang_toggle_home"):
            st.session_state.telugu_home = not is_telugu_home
            st.rerun()
    
    st.image(load_and_resize_image("images/dentist/Logo.jpg", 800, 300), use_container_width=True)
    
    if is_telugu_home:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px;">
            <h3 style="text-align: center; color: #2c3e50;">మంచి దంత ఆరోగ్యానికి మొదటి మెట్టు</h3>
            <p style="text-align: justify;">
సింప్టోడెంట్ (SymptoDent) అనేది నేను నోటి ఆరోగ్యంపై అవగాహనను మెరుగుపరచడానికి ఒక ప్రాక్టీసింగ్ దంతవైద్యునిగా సృష్టించిన స్వీయ-సహాయ దంత నిర్ధారణ మరియు విద్యా యాప్. నోటి ఆరోగ్యంపై అవగాహనను మెరుగుపరచడం దీని లక్ష్యం. వినియోగదారులు 20 సాధారణ లక్షణాల నుండి ఎంచుకొని, సంభావ్య సమస్యలను గుర్తించగలరు, ఏ నిపుణుడిని సంప్రదించాలో మార్గదర్శకత్వం పొందుతారు, మరియు బ్రషింగ్ పద్ధతులు, చికిత్స అనంతర సంరక్షణపై విద్యాపరమైన కంటెంట్‌ను యాక్సెస్ చేయగలరు. తక్కువ అక్షరాస్యత ఉన్న ప్రదేశాలలో కూడా సులభంగా అందుబాటులో ఉండటానికి, ప్రజలకు విద్యను అందించడానికి మరియు మార్గనిర్దేశం చేయడానికి ఇది ఇంగ్లీష్ మరియు తెలుగు భాషలలో రూపొందించబడింది. ప్రస్తుతం, ఇది కార్మికులు మరియు పాఠశాల విద్యార్థుల మధ్య పరీక్షించబడుతోంది. ఈ చొరవ ముఖ్యంగా తక్కువ సేవలు ఉన్న కమ్యూనిటీలలో, లక్షణాల గుర్తింపు మరియు సకాలంలో దంత సంరక్షణ మధ్య ఉన్న అంతరాన్ని తగ్గించడానికి ఉద్దేశించబడింది.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("లక్షణాలను అన్వేషించండి →", type="primary"):
            st.session_state.page = "symptom_explorer"
            st.rerun()
    else:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px;">
            <h3 style="text-align: center; color: #2c3e50;">Your first step to smarter dental health</h3>
            <p style="text-align: justify;">
                Symptodent is a self-help dental diagnosis and education app I created as a practicing dentist to improve oral health awareness. Users select from 20 common symptoms to identify probable conditions, receive guidance on which specialist to consult, and access educational content on brushing techniques and post-treatment care. Built for educating and guiding the general public in English & Telugu for accessibility in low-literacy settings. It is currently being tested among working-class individuals and school students. This initiative aims to bridge the gap between symptom recognition and timely dental care, especially in underserved communities.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Explore Symptoms →", type="primary"):
            st.session_state.page = "symptom_explorer"
            st.rerun()

def show_symptom_explorer():
    st.title("Symptom Explorer")
    st.write("Select any symptom below to view detailed information.")
    
    cols_per_row = 3
    cols = st.columns(cols_per_row)
    
    for i, (symptom_key, symptom_data) in enumerate(symptoms_data.items()):
        with cols[i % cols_per_row]:
            img = load_and_resize_image(symptom_data["image"])
            
            st.markdown(f"""
            <div class="uniform-card">
                <img src="data:image/png;base64,{image_to_base64(img)}" alt="{symptom_key}">
                <h4>{symptom_key}</h4>
                <p>{symptom_data['Symptom']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown('<div class="button-container">', unsafe_allow_html=True)
            if st.button("View Details", key=f"btn_{symptom_key}"):
                st.session_state.page = "symptom_details"
                st.session_state.current_symptom = symptom_key
                st.rerun()
            if st.button("Post Care", key=f"post_{symptom_key}"):
                st.session_state.page = "post_treatment_care"
                st.session_state.current_symptom = symptom_key
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🏠 Back to Home"):
        st.session_state.page = "home"
        st.rerun()

def show_symptom_details(symptom_key):
    symptom = symptoms_data[symptom_key]
    is_telugu = st.session_state.get(f"telugu_{symptom_key}", False)
    
    st.title(symptom["telugu"]["name"] if is_telugu else symptom_key)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        img = load_and_resize_image(symptom["image"], 400, 300)
        st.image(img, use_container_width=True)
        
        if st.button("తెలుగులో చూడండి" if not is_telugu else "View in English", 
                    key=f"lang_toggle_{symptom_key}"):
            st.session_state[f"telugu_{symptom_key}"] = not is_telugu
            st.rerun()
    
    with col2:
        with st.container():
            st.markdown('<div class="info-box">', unsafe_allow_html=True)
            st.subheader("లక్షణం" if is_telugu else "Symptom")
            st.info(symptom["telugu"]["Symptom"] if is_telugu else symptom["Symptom"])
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="info-box">', unsafe_allow_html=True)
            st.subheader("కాలం" if is_telugu else "Duration")
            st.info(symptom["telugu"]["duration"] if is_telugu else symptom["duration"])
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="warning-box">', unsafe_allow_html=True)
            st.subheader("సంభావ్య సమస్య" if is_telugu else "Probable Condition")
            st.warning(symptom["telugu"]["probable condition"] if is_telugu else symptom["probable condition"])
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="success-box">', unsafe_allow_html=True)
            st.subheader("సలహాలు" if is_telugu else "Advice")
            st.success(symptom["telugu"]["advice"] if is_telugu else symptom["advice"])
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="error-box">', unsafe_allow_html=True)
            st.subheader("సూచించిన వైద్యుడు" if is_telugu else "Referral")
            st.error(symptom["telugu"]["referral"] if is_telugu else symptom["referral"])
            st.markdown('</div>', unsafe_allow_html=True)
    
    col3, col5 = st.columns(2)
    with col3:
        if st.button("📚 Learn More (External Link)", key=f"learn_{symptom_key}"):
            webbrowser.open_new_tab(symptom["learn more"])
    with col5:
        if st.button("🩺 Post Treatment Care", key=f"postcare_{symptom_key}"):
            st.session_state.page = "post_treatment_care"
            st.session_state.current_symptom = symptom_key
            st.rerun()
    
    if st.button("← వెనక్కి వెళ్లండి" if is_telugu else "← Back to Symptom Explorer"):
        st.session_state.page = "symptom_explorer"
        st.rerun()

def show_post_treatment_care(symptom_key):
    symptom = symptoms_data[symptom_key]
    post_care = symptom.get("post_treatment_care", {})
    is_telugu = st.session_state.get(f"telugu_{symptom_key}", False)
    
    st.title(f"{symptom['telugu']['name'] if is_telugu else symptom_key} - Post Treatment Care")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        img = load_and_resize_image(symptom["image"], 400, 300)
        st.image(img, use_container_width=True)
        
        if st.button("తెలుగులో చూడండి" if not is_telugu else "View in English", 
                    key=f"lang_toggle_{symptom_key}"):
            st.session_state[f"telugu_{symptom_key}"] = not is_telugu
            st.rerun()
    
    with col2:
        with st.container():
            st.markdown('<div class="info-box">', unsafe_allow_html=True)
            st.subheader("తక్షణాన చికిత్స సూచనలు" if is_telugu else "Immediate Post-Treatment Care")
            st.info(post_care.get("Immediate Post-Treatment Care", {}).get("Telugu" if is_telugu else "English", "Information not available"))
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="info-box">', unsafe_allow_html=True)
            st.subheader("ఔషధాలు" if is_telugu else "Medications")
            st.info(post_care.get("Medications", {}).get("Telugu" if is_telugu else "English", "Information not available"))
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="warning-box">', unsafe_allow_html=True)
            st.subheader("ఆహారం మరియు జీవనశైలి" if is_telugu else "Diet & Lifestyle")
            st.warning(post_care.get("Diet & Lifestyle", {}).get("Telugu" if is_telugu else "English", "Information not available"))
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="success-box">', unsafe_allow_html=True)
            st.subheader("నోటి పరిశుభ్రత" if is_telugu else "Oral Hygiene")
            st.success(post_care.get("Oral Hygiene", {}).get("Telugu" if is_telugu else "English", "Information not available"))
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="error-box">', unsafe_allow_html=True)
            st.subheader("అనుసరణ పర్యవేక్షణ" if is_telugu else "Follow-Up")
            st.error(post_care.get("Follow-Up", {}).get("Telugu" if is_telugu else "English", "Information not available"))
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="error-box">', unsafe_allow_html=True)
            st.subheader("తక్షణ సహాయం కోరాల్సిన పరిస్థితులు" if is_telugu else "Seek Immediate Help If")
            st.error(post_care.get("Seek Immediate Help If", {}).get("Telugu" if is_telugu else "English", "Information not available"))
            st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("← వెనక్కి వెళ్లండి" if is_telugu else "← Back to Symptom Details"):
        st.session_state.page = "symptom_details"
        st.rerun()

def show_education():
    st.title("📚 Dental Education Resources")
    
    # Language toggle for education section
    is_telugu_education = st.session_state.get("telugu_education", False)
    
    if st.button("తెలుగులో చూడండి" if not is_telugu_education else "View in English", 
                key="lang_toggle_education"):
        st.session_state["telugu_education"] = not is_telugu_education
        st.rerun()
    
    if is_telugu_education:
        # Telugu content for education section
        with st.container():
            st.header("🪥 బ్రష్ చేయడం యొక్క సాధారణ మార్గదర్శకాలు")
            st.image("images/dentist/brush technique.jpg", 
                    caption="సరైన బ్రషింగ్ పద్ధతి", width=300)
            st.markdown("""
            - **రోజుకు రెండుసార్లు బ్రష్ చేయండి** - ఉదయం మరియు నిద్రకు ముందు
            - **మృదువైన బ్రష్** మరియు **ఫ్లోరైడ్ టూత్పేస్ట్** వాడండి
            - ప్రతి సారి **కనీసం 2 నిమిషాలు** బ్రష్ చేయండి
            - **అన్ని దంత ఉపరితలాలను** కవర్ చేయండి: బయటి, లోపలి మరియు నమలే భాగాలు
            - ప్రతి **3 నెలలకు** బ్రష్ మార్చండి లేదా బ్రష్ తలలు విడిపోతే
            """)
            
            st.divider()
            
            # Flossing Technique in Telugu
            st.header("🧵 ఫ్లోసింగ్ పద్ధతి")
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image("images/dentist/flos.jpg",
                       caption="సరైన ఫ్లోసింగ్ పద్ధతి", width=200)
            with col2:
                st.markdown("""
                ఫ్లోసింగ్ దంతాల మధ్య ఉండే ప్లాక్‌ను తొలగిస్తుంది, బ్రష్ చేయలేని ప్రదేశాల్లో.
                
                - **18 అంగుళాల** డెంటల్ ఫ్లోస్ వాడండి
                - దంతాల మధ్య **మృదువుగా ప్రవేశపెట్టండి**
                - ప్రతి దంతం చుట్టూ **"C" ఆకారంలో** వంచండి
                - **పైకి కిందికి** కొన్ని సార్లు కదిలించండి
                
                **ప్రత్యామ్నాయాలు:**
                - ఫ్లోస్ పిక్స్
                - వాటర్ ఫ్లోసర్లు
                - ఇంటర్‌డెంటల్ బ్రష్‌లు
                """)
            
            st.divider()
            
            # Mouthwash Use in Telugu
            st.header("💧 మౌత్‌వాష్ వాడకం")
            st.image("images/dentist/mouthwash.jpg",
                    caption="మౌత్‌వాష్ సరిగ్గా వాడటం", width=300)
            st.markdown("""
            - **ఆల్కహాల్ లేని**, ఫ్లోరైడ్ కలిగిన మౌత్‌వాష్ వాడండి
            - **10–15 మి.లీ.** తో **30–60 సెకన్లు** పుక్కిలించండి
            - **బ్రషింగ్ మరియు ఫ్లోసింగ్ తర్వాత** వాడండి
            - వాడిన తర్వాత **30 నిమిషాలు** ఆహారం/పానీయాలు తీసుకోకండి
            - **6 సంవత్సరాల కంటే తక్కువ** వయస్సు పిల్లలకు సిఫార్సు చేయరు
            """)
            
            st.divider()
            
            # Age-wise Oral Care in Telugu
            st.header("👶👧👩👴 వయస్సు వారీగా నోటి సంరక్షణ మార్గదర్శకాలు")
            tab_infants, tab_toddlers, tab_children, tab_teens, tab_adults, tab_seniors = st.tabs(
                ["శిశువులు", "చిన్న పిల్లలు", "పిల్లలు", "యువత", "పెద్దలు", "వృద్ధులు"])
            
            with tab_infants:
                st.subheader("శిశువులు (0–2 సంవత్సరాలు)")
                st.image("images/dentist/infant.jpg",
                       width=200)
                st.markdown("""
                - **చిగుళ్ళను శుభ్రంగా తడి గుడ్డతో తుడవండి**
                - **మొదటి పళ్ళు** వచ్చిన తర్వాత బ్రషింగ్ ప్రారంభించండి
                - **18 నెలల లోపు** ఫ్లోరైడ్ టూత్‌పేస్ట్ వాడకండి
                - **రాత్రి సమయంలో బాటిల్ ఫీడింగ్** నివారించండి
                """)
            
            with tab_toddlers:
                st.subheader("చిన్న పిల్లలు (2–6 సంవత్సరాలు)")
                st.image("images/dentist/toddler.jpg",
                       width=200)
                st.markdown("""
                - **స్మియర్ పరిమాణంలో** ఫ్లోరైడ్ టూత్‌పేస్ట్ వాడండి
                - **సర్క్యులర్ బ్రషింగ్** (ఫోన్స్ టెక్నిక్) చూసుకోండి
                - టూత్‌పేస్ట్ **మింగకూడదని** నేర్పండి
                - **1 సంవత్సరం వయస్సులోపు** మొదటి దంత పరీక్ష
                """)
                
            with tab_children:
                st.subheader("పిల్లలు (7–12 సంవత్సరాలు)")
                st.image("images/dentist/children.jpg",
                       width=200)
                st.markdown("""
                - **మటుకు పరిమాణంలో** ఫ్లోరైడ్ టూత్‌పేస్ట్ వాడండి
                - **బాస్ టెక్నిక్** (కోణంలో బ్రషింగ్) నేర్పండి
                - **నియమితంగా ఫ్లోసింగ్** ప్రారంభించండి
                - ప్రతి **6 నెలలకు** డెంటిస్ట్‌ను సంప్రదించండి
                """)
                
            with tab_teens:
                st.subheader("యువత (13–19 సంవత్సరాలు)")
                st.image("images/dentist/teen.jpg",
                       width=200)
                st.markdown("""
                - **భోజనం తర్వాత** బ్రష్ చేయడానికి ప్రయత్నించండి
                - రోజూ **ఫ్లోస్ మరియు మౌత్‌వాష్** వాడండి
                - **ఆర్థోడాంటిక్ పరీక్ష** పరిగణించండి
                - **పొగ మరియు నోటి పియర్సింగ్స్** నివారించండి
                """)
                
            with tab_adults:
                st.subheader("పెద్దలు (20–59 సంవత్సరాలు)")
                st.image("images/dentist/adult.jpg",
                       width=200)
                st.markdown("""
                - **పూర్తి నోటి పరిశుభ్రత** రూటిన్ పాటించండి
                - **చిగుళ్ళ వ్యాధుల** ప్రారంభ లక్షణాలను గమనించండి
                - **పొగ/మద్యపానం** తగ్గించండి
                - **రెగ్యులర్ డెంటల్ చెకప్‌లు**
                """)
                
            with tab_seniors:
                st.subheader("వృద్ధులు (60+ సంవత్సరాలు)")
                st.image("images/dentist/old.jpg",
                       width=200)
                st.markdown("""
                - **ఎలక్ట్రిక్ బ్రష్** లేదా మృదువైన బ్రష్ వాడండి
                - **డెంచర్‌లను రోజూ** శుభ్రం చేయండి
                - **నోరు పొడిగా ఉంటే** తేమ కోసం ప్రత్యామ్నాయాలు వాడండి
                - **నోటి గాయాలు** మరియు దంత కదలికను గమనించండి
                """)
            
            st.divider()
            
            # Harmful Habits in Telugu
            st.header("🚭 నివారించాల్సిన హానికరమైన అలవాట్లు")
            st.image("images/dentist/harmful.jpg",
                   caption="నివారించాల్సిన హానికరమైన అలవాట్లు", width=400)
            cols = st.columns(2)
            with cols[0]:
                st.markdown("""
                - పొగతాగడం/మిలమిలా తాగడం
                - మద్యపాన దుర్వినియోగం
                - నోటి పరిశుభ్రతను విస్మరించడం
                - ఎక్కువ గట్టిగా బ్రష్ చేయడం
                """)
            with cols[1]:
                st.markdown("""
                - పళ్ళను సాధనాలుగా ఉపయోగించడం
                - గోర్లు కొరుకడం
                - గట్టి పదార్థాలు నమలడం
                - తరచుగా తీపి ఆహారం తీసుకోవడం
                """)
            
            st.divider()
            
            # Supplements in Telugu
            st.header("💊 సిఫార్సు చేయబడిన సప్లిమెంట్స్ మరియు జాగ్రత్తలు")
            st.image("images/dentist/supplements.jpg",
                   width=300)
            st.markdown("""
            - **విటమిన్ సి**: చిగుళ్ళ ఆరోగ్యానికి సహాయపడుతుంది
            - **కాల్షియం & విటమిన్ డి**: దంతాలను బలపరుస్తుంది
            - **ఫ్లోరైడ్ సప్లిమెంట్స్**: వైద్యుడు సిఫార్సు చేసినప్పుడు మాత్రమే
            - **గమ్‌లపై ఆస్పిరిన్ వేయకండి** (కాలుస్తుంది)
            - **అలర్జీల గురించి** డెంటిస్ట్‌కు తెలియజేయండి
            - **లవంగ తైలం**: తాత్కాలిక నొప్పి నివారణకు మాత్రమే
            """)
    else:
        # Original English content for education section
        with st.container():
            st.header("🪥 General Brushing Guidelines")
            st.image("images/dentist/brush technique.jpg", 
                    caption="Proper brushing technique", width=300)
            st.markdown("""
            - **Brush twice daily** – in the morning and before bed
            - Use a **soft-bristled toothbrush** and **fluoride toothpaste**
            - Brush for **at least 2 minutes** each session
            - Cover **all tooth surfaces**: outer, inner, and chewing
            - Replace your toothbrush **every 3 months** or when bristles fray
            """)
            
            st.divider()
            
            # Flossing Technique
            st.header("🧵 Flossing Technique")
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image("images/dentist/flos.jpg",
                       caption="Proper flossing technique", width=200)
            with col2:
                st.markdown("""
                Flossing removes plaque from between teeth where brushes can't reach.
                
                - Use **18 inches** of dental floss
                - Gently **guide between teeth**
                - Curve into **"C" shape** around each tooth
                - Slide **up and down** several times
                
                **Alternatives:**
                - Floss picks
                - Water flossers
                - Interdental brushes
                """)
            
            st.divider()
            
            # Mouthwash Use
            st.header("💧 Mouthwash Use")
            st.image("images/dentist/mouthwash.jpg",
                    caption="Using mouthwash correctly", width=300)
            st.markdown("""
            - Use **alcohol-free**, fluoride-containing mouthwash
            - Rinse with **10–15 mL** for **30–60 seconds**
            - Use **after brushing and flossing**
            - Avoid food/drink for **30 minutes** after
            - **Not recommended** for children under 6
            """)
            
            st.divider()
            
            # Age-wise Oral Care
            st.header("👶👧👩👴 Age-wise Oral Care Guidelines")
            tab_infants, tab_toddlers, tab_children, tab_teens, tab_adults, tab_seniors = st.tabs(
                ["Infants", "Toddlers", "Children", "Teens", "Adults", "Seniors"])
            
            with tab_infants:
                st.subheader("Infants (0–2 years)")
                st.image("images/dentist/infant.jpg",
                       width=200)
                st.markdown("""
                - Wipe gums with **clean, damp cloth**
                - Start brushing with **first tooth**
                - **No fluoride toothpaste** under 18 months
                - Avoid **bedtime bottle feeding**
                """)
            
            with tab_toddlers:
                st.subheader("Toddlers (2–6 years)")
                st.image("images/dentist/toddler.jpg",
                       width=200)
                st.markdown("""
                - Use **smear** of fluoride toothpaste
                - Supervise **circular brushing** (Fones technique)
                - Teach not to **swallow toothpaste**
                - First dental visit **by age 1**
                """)
                
            with tab_children:
                st.subheader("Children (7–12 years)")
                st.image("images/dentist/children.jpg",
                       width=200)
                st.markdown("""
                - Use **pea-sized** fluoride toothpaste
                - Teach **Bass technique** (angled brushing)
                - Begin **regular flossing**
                - Dental visits **every 6 months**
                """)
                
            with tab_teens:
                st.subheader("Teenagers (13–19 years)")
                st.image("images/dentist/teen.jpg",
                       width=200)
                st.markdown("""
                - Brush **after every meal** if possible
                - Daily **floss and mouthwash**
                - Consider **orthodontic evaluation**
                - Avoid **tobacco and oral piercings**
                """)
                
            with tab_adults:
                st.subheader("Adults (20–59 years)")
                st.image("images/dentist/adult.jpg",
                       width=200)
                st.markdown("""
                - Maintain **complete oral routine**
                - Watch for **gum disease** signs
                - Limit **tobacco/alcohol**
                - Regular **dental checkups**
                """)
                
            with tab_seniors:
                st.subheader("Elderly (60+ years)")
                st.image("images/dentist/old.jpg",
                       width=200)
                st.markdown("""
                - Use **electric toothbrushes**
                - Clean **dentures daily**
                - **Hydrate mouth** regularly
                - Monitor for **oral lesions**
                """)
            
            st.divider()
            
            # Harmful Habits
            st.header("🚭 Harmful Habits to Avoid")
            st.image("images/dentist/harmful.jpg",
                   caption="Damaging habits to avoid", width=400)
            cols = st.columns(2)
            with cols[0]:
                st.markdown("""
                - Smoking/chewing tobacco
                - Alcohol abuse
                - Skipping oral hygiene
                - Brushing too hard
                """)
            with cols[1]:
                st.markdown("""
                - Using teeth as tools
                - Nail biting
                - Chewing ice/hard objects
                - Frequent sugary snacks
                """)
            
            st.divider()
            
            # Supplements
            st.header("💊 Recommended Supplements & Cautions")
            st.image("images/dentist/supplements.jpg",
                   width=300)
            st.markdown("""
            - **Vitamin C**: Supports gum health
            - **Calcium & Vitamin D**: Strengthens teeth
            - **Fluoride supplements**: Only if prescribed
            - Avoid **aspirin on gums** (causes burns)
            - Inform dentist about **allergies**
            - **Clove oil**: Temporary pain relief only
            """)
   
    if st.button("← వెనక్కి వెళ్లండి" if is_telugu_education else "← Back to Home"):
        st.session_state.page = "home"
        st.rerun()

# IMPORTANT: Replace these with your actual Google Form links
ENGLISH_GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSflYg-Jd3bohdLaCF3MI61PkYL8lWRttFPJxxBAfRJXrDWamA/viewform?usp=dialog"
TELUGU_GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScvKODWw0RMMM8fLzyt5YQYk_IniaEqkGepuGHhHEtyau_jCg/viewform?usp=header"
# ---

# Define text content for both languages
TEXT_CONTENT = {
    "en": {
        "title": "We'd Love Your Feedback! 💬",
        "intro": "Your input helps us improve! Please take a moment to share your thoughts, suggestions, or any issues you've encountered.",
        "button_text": "Open Feedback Form",
        "thanks": "Thank you for helping us make this application better for everyone!",
        "language_toggle_label": "Switch to Telugu"
    },
    "te": {
        "title": "మీ అభిప్రాయాన్ని మేము స్వీకరించాలనుకుంటున్నాము! 💬",
        "intro": "మీ అభిప్రాయం మాకు మెరుగుపరచడానికి సహాయపడుతుంది! దయచేసి మీ ఆలోచనలు, సూచనలు లేదా మీరు ఎదుర్కొన్న ఏవైనా సమస్యలను పంచుకోవడానికి కొంత సమయం కేటాయించండి.",
        "button_text": "అభిప్రాయ ఫారమ్ తెరవండి",
        "thanks": "ప్రతి ఒక్కరికీ ఈ అప్లికేషన్‌ను మెరుగుపరచడంలో మాకు సహాయం చేసినందుకు ధన్యవాదాలు!",
        "language_toggle_label": "ఇంగ్లీష్‌కి మార్చండి"
    }
}

# Ensure session state is initialized for language
if 'language' not in st.session_state:
    st.session_state.language = 'en' # Default language is English

def show_feedback():
    # Language Toggle
    # The toggle's value directly reflects if Telugu is active
    is_telugu_active = st.toggle(
        TEXT_CONTENT[st.session_state.language]["language_toggle_label"],
        value=(st.session_state.language == 'te'),
        key="language_toggle"
    )

    # Update session state based on toggle
    if is_telugu_active:
        st.session_state.language = 'te'
    else:
        st.session_state.language = 'en'

    # Get current language content
    current_lang = st.session_state.language
    content = TEXT_CONTENT[current_lang]
    form_link = ENGLISH_GOOGLE_FORM_LINK if current_lang == 'en' else TELUGU_GOOGLE_FORM_LINK

    st.title(content["title"])
    
    st.write(content["intro"])

    # Styled button for the feedback form
    st.markdown(
        f"""
        <a href="{form_link}" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 8px; border: none; cursor: pointer; transition: background-color 0.3s ease;">
            {content["button_text"]}
        </a>
        """,
        unsafe_allow_html=True
    )
    
    st.write(
        f"""
        ---
        {content["thanks"]}
        """
    )
# Main App Router
if st.session_state.page == "home":
    show_home()
elif st.session_state.page == "symptom_explorer":
    show_symptom_explorer()
elif st.session_state.page == "symptom_details":
    show_symptom_details(st.session_state.current_symptom)
elif st.session_state.page == "post_treatment_care":
    show_post_treatment_care(st.session_state.current_symptom)
elif st.session_state.page == "education":
    show_education()
elif st.session_state.page == "feedback":
    show_feedback()