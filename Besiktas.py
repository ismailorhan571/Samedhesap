import streamlit as st
import streamlit.components.v1 as components

# 1. Sayfa Ayarları
st.set_page_config(page_title="Kara Kartal Pro", page_icon="🦅", layout="centered")

# 2. HTML ve JS Kodu (Hesap Makinesi Gövdesi)
calc_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { background-color: #000; font-family: -apple-system, sans-serif; display: flex; justify-content: center; padding-top: 5px; overflow: hidden; margin: 0; }
        .calc-body { width: 330px; background-color: #000; border-radius: 20px; padding: 10px; position: relative; }
        
        /* BJK Logo - Sol Üstte Çerçevesiz */
        .bjk-logo {
            position: absolute; top: 10px; left: 10px;
            width: 55px; height: 55px;
            background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Logo_of_Be%C5%9Fikta%C5%9F_JK.svg/1920px-Logo_of_Be%C5%9Fikta%C5%9F_JK.svg.png');
            background-size: contain; background-repeat: no-repeat;
            z-index: 100;
        }

        #display {
            width: 100%; height: 85px; background: #000; color: white;
            text-align: right; font-size: 48px; border: none; margin-bottom: 10px; outline: none;
            padding-right: 10px; box-sizing: border-box;
        }
        .grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; }
        button {
            height: 58px; width: 100%; border-radius: 50%; border: none;
            font-size: 16px; font-weight: bold; cursor: pointer; transition: 0.1s;
            display: flex; justify-content: center; align-items: center;
        }
        button:active { opacity: 0.6; transform: scale(0.92); }
        
        /* BJK Renk Şeması */
        .num { background-color: #333333; color: white; }
        .op { background-color: #a5a5a5; color: black; font-size: 22px; } 
        .func { background-color: #FFFFFF; color: black; font-size: 18px; } 
        .spec { background-color: #1a1a1a; color: #FFFFFF; font-size: 14px; border: 1px solid #444; }
        .equal { background-color: #FFFFFF; color: #000; font-size: 24px; }
        
        /* Kırmızı Detaylar (Feda) */
        .feda { background-color: #E30613 !important; color: white !important; }
    </style>
</head>
<body>
    <div class="calc-body">
        <div class="bjk-logo"></div>
        <input type="text" id="display" value="0" disabled>
        
        <div class="grid">
            <button class="spec" onclick="add('**')">xʸ</button>
            <button class="spec feda" onclick="sqrt()">√x</button>
            <button class="spec" onclick="add('**2')">x²</button>
            <button class="func" onclick="cls()">AC</button>
            <button class="op" onclick="add('/')">÷</button>
            
            <button class="num" onclick="add('7')">7</button>
            <button class="num" onclick="add('8')">8</button>
            <button class="num" onclick="add('9')">9</button>
            <button class="func" onclick="del()">DEL</button>
            <button class="op" onclick="add('*')">×</button>
            
            <button class="num" onclick="add('4')">4</button>
            <button class="num" onclick="add('5')">5</button>
            <button class="num" onclick="add('6')">6</button>
            <button class="num" onclick="add('%')">%</button>
            <button class="op" onclick="add('-')">−</button>
            
            <button class="num" onclick="add('1')">1</button>
            <button class="num" onclick="add('2')">2</button>
            <button class="num" onclick="add('3')">3</button>
            <button class="num" onclick="add('.')">.</button>
            <button class="op" onclick="add('+')">+</button>
            
            <button class="num" style="grid-column: span 2; border-radius: 30px;" onclick="add('0')">0</button>
            <button style="visibility: hidden;"></button>
            <button class="equal feda" style="grid-column: span 2; border-radius: 30px;" onclick="calc()">=</button>
        </div>
    </div>

    <script>
        let disp = document.getElementById('display');
        function add(v) { 
            if(disp.value == '0' || disp.value == 'Hata') disp.value = v;
            else disp.value += v;
        }
        function cls() { disp.value = '0'; }
        function del() { disp.value = disp.value.slice(0,-1); if(disp.value=='') disp.value='0'; }
        function sqrt() { try { disp.value = Math.sqrt(eval(disp.value)).toFixed(2); } catch { disp.value = 'Hata'; } }
        function calc() {
            try { 
                let res = eval(disp.value);
                disp.value = Number.isInteger(res) ? res : res.toFixed(4);
            }
            catch { disp.value = 'Hata'; }
        }
    </script>
</body>
</html>
"""

# 3. YENİ SİYAH VE PARLAK BAŞLIK
# Renk siyah (#000) yapıldı, ancak görünmesi için beyaz parlama (text-shadow) eklendi.
st.markdown(
    """
    <h2 style='text-align: center; color: #000; font-family: sans-serif; 
               text-shadow: 0 0 10px #fff, 0 0 20px #fff; 
               background: rgba(255,255,255,0.1); border-radius: 10px; padding: 5px;'>
        🦅 KARA KARTAL PRO 🦅
    </h2>
    """, 
    unsafe_allow_html=True
)

# 4. Hesap Makinesi
components.html(calc_html, height=480)

# 5. Alt İmza
st.markdown("<h3 style='text-align: center; color: white; margin-top: 0;'>Geliştiren: İsmail Orhan</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; font-size: 14px;'>Kara Kartal Ruhu İsmail Abisinden Samed kardeşime özel 
</p>", unsafe_allow_html=True)
