import streamlit as st
import random
from datetime import datetime

# Cấu hình trang
st.set_page_config(page_title="Công nghệ Kỹ thuật - Học tập", page_icon="🎓", layout="wide")

# CSS tùy chỉnh
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1e88e5;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .lesson-card {
        border: 2px solid #e3f2fd;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        background: #f5f5f5;
    }
    .quiz-option {
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
        background: #e3f2fd;
    }
    .success-box {
        padding: 15px;
        background: #c8e6c9;
        border-radius: 5px;
        margin: 10px 0;
    }
    .error-box {
        padding: 15px;
        background: #ffcdd2;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Tiêu đề chính
st.markdown("<h1 class='main-header'>🎓 Công nghệ Kỹ thuật - Tool Học tập</h1>", unsafe_allow_html=True)

# Khởi tạo session state
if 'current_lesson' not in st.session_state:
    st.session_state.current_lesson = None
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}
if 'completed_lessons' not in st.session_state:
    st.session_state.completed_lessons = []

# Nội dung bài học
LESSONS = {
    "Cơ bản về Điện tử": {
        "icon": "⚡",
        "content": """
        ### Giới thiệu về Điện tử
        
        **1. Điện tử là gì?**
        - Điện tử học là ngành khoa học nghiên cứu về dòng chảy và điều khiển electron
        - Ứng dụng trong máy tính, điện thoại, TV và nhiều thiết bị khác
        
        **2. Các linh kiện cơ bản:**
        
        **Điện trở (Resistor):**
        - Ký hiệu: R
        - Đơn vị: Ohm (Ω)
        - Chức năng: Hạn chế dòng điện
        - Công thức: V = I × R (Định luật Ohm)
        
        **Tụ điện (Capacitor):**
        - Ký hiệu: C
        - Đơn vị: Farad (F)
        - Chức năng: Lưu trữ năng lượng điện
        
        **Cuộn cảm (Inductor):**
        - Ký hiệu: L
        - Đơn vị: Henry (H)
        - Chức năng: Lưu trữ năng lượng từ trường
        
        **Điốt (Diode):**
        - Cho phép dòng điện chạy một chiều
        - Dùng để chỉnh lưu AC sang DC
        
        **Transistor:**
        - Thiết bị bán dẫn 3 chân
        - Dùng để khuếch đại hoặc đóng/ngắt tín hiệu
        - Là nền tảng của vi xử lý hiện đại
        
        **3. Mạch điện cơ bản:**
        - Mạch nối tiếp: I giống nhau, V chia theo tỉ lệ
        - Mạch song song: V giống nhau, I chia theo tỉ lệ
        
        **4. Ví dụ thực tế:**
        - LED: Đèn phát sáng khi có dòng điện
        - Arduino: Vi điều khiển để học lập trình điện tử
        - Cảm biến: Chuyển đổi đại lượng vật lý thành tín hiệu điện
        """,
        "resources": [
            "📚 Sách: 'Điện tử cơ bản' - Paul Scherz",
            "🎥 YouTube: 'Electronics Tutorials'",
            "🔗 Website: electronics-tutorials.ws"
        ]
    },
    
    "Lập trình cơ bản": {
        "icon": "💻",
        "content": """
        ### Giới thiệu về Lập trình
        
        **1. Lập trình là gì?**
        - Là quá trình tạo ra các chương trình máy tính
        - Sử dụng ngôn ngữ lập trình để ra lệnh cho máy tính
        
        **2. Các ngôn ngữ lập trình phổ biến:**
        
        **Python:**
        ```python
        # Chương trình Hello World
        print("Xin chào!")
        
        # Biến và phép toán
        so_a = 10
        so_b = 5
        tong = so_a + so_b
        print(f"Tổng: {tong}")
        
        # Vòng lặp
        for i in range(5):
            print(f"Lần {i+1}")
        ```
        
        **JavaScript:**
        ```javascript
        // Hàm cơ bản
        function chaoHoi(ten) {
            console.log("Xin chào " + ten);
        }
        
        // Mảng
        let danhSach = [1, 2, 3, 4, 5];
        danhSach.forEach(num => console.log(num));
        ```
        
        **3. Các khái niệm quan trọng:**
        
        **Biến (Variables):**
        - Lưu trữ dữ liệu
        - Có kiểu dữ liệu: số, chuỗi, boolean
        
        **Điều kiện (If/Else):**
        ```python
        diem = 8
        if diem >= 5:
            print("Đạt")
        else:
            print("Không đạt")
        ```
        
        **Vòng lặp (Loops):**
        - For: lặp với số lần xác định
        - While: lặp khi điều kiện đúng
        
        **Hàm (Functions):**
        - Khối code có thể tái sử dụng
        - Nhận tham số, trả về kết quả
        
        **4. Thuật toán cơ bản:**
        - Tìm kiếm tuần tự
        - Sắp xếp nổi bọt
        - Tìm kiếm nhị phân
        
        **5. Dự án thực hành:**
        - Máy tính đơn giản
        - Game đoán số
        - Quản lý danh sách việc cần làm
        """,
        "resources": [
            "📚 Sách: 'Python cho người mới bắt đầu'",
            "🎥 YouTube: 'Lập trình không khó'",
            "🔗 Website: codecademy.com, freecodecamp.org"
        ]
    },
    
    "Mạng máy tính": {
        "icon": "🌐",
        "content": """
        ### Giới thiệu về Mạng máy tính
        
        **1. Mạng máy tính là gì?**
        - Hệ thống kết nối các thiết bị với nhau
        - Cho phép chia sẻ dữ liệu và tài nguyên
        
        **2. Mô hình OSI (7 lớp):**
        1. **Vật lý**: Truyền bit qua môi trường vật lý
        2. **Liên kết dữ liệu**: Truyền frame giữa 2 node
        3. **Mạng**: Định tuyến packet (IP)
        4. **Giao vận**: Truyền dữ liệu end-to-end (TCP/UDP)
        5. **Phiên**: Quản lý phiên kết nối
        6. **Trình bày**: Mã hóa/giải mã dữ liệu
        7. **Ứng dụng**: Giao diện người dùng (HTTP, FTP)
        
        **3. Địa chỉ IP:**
        - IPv4: 192.168.1.1 (32 bit)
        - IPv6: 2001:0db8:85a3::8a2e:0370:7334 (128 bit)
        - Subnet mask: Phân chia mạng
        
        **4. Các giao thức quan trọng:**
        
        **HTTP/HTTPS:**
        - Giao thức web
        - HTTPS có mã hóa SSL/TLS
        
        **TCP vs UDP:**
        - TCP: Đáng tin cậy, có xác nhận
        - UDP: Nhanh, không xác nhận
        
        **DNS:**
        - Chuyển tên miền thành địa chỉ IP
        - Ví dụ: google.com → 142.250.185.78
        
        **5. Thiết bị mạng:**
        - **Router**: Định tuyến giữa các mạng
        - **Switch**: Kết nối thiết bị trong mạng LAN
        - **Modem**: Chuyển đổi tín hiệu số/analog
        - **Access Point**: Phát WiFi
        
        **6. Bảo mật mạng:**
        - Firewall: Lọc traffic
        - VPN: Mạng riêng ảo
        - Mã hóa: WPA2, WPA3
        - HTTPS: SSL/TLS certificate
        
        **7. Công cụ kiểm tra:**
        - ping: Kiểm tra kết nối
        - traceroute: Theo dõi đường đi
        - netstat: Xem kết nối mạng
        - wireshark: Phân tích gói tin
        """,
        "resources": [
            "📚 Sách: 'Computer Networking' - Andrew Tanenbaum",
            "🎥 YouTube: 'NetworkChuck', 'Eli the Computer Guy'",
            "🔗 Website: cisco.com/learning"
        ]
    },
    
    "Cơ học Robot": {
        "icon": "🤖",
        "content": """
        ### Giới thiệu về Robot và Tự động hóa
        
        **1. Robot là gì?**
        - Máy móc có thể được lập trình để thực hiện các tác vụ
        - Kết hợp cơ khí, điện tử và lập trình
        
        **2. Các thành phần của Robot:**
        
        **Cảm biến (Sensors):**
        - Cảm biến khoảng cách (Ultrasonic)
        - Cảm biến ánh sáng (LDR)
        - Cảm biến nhiệt độ (LM35)
        - Cảm biến chuyển động (PIR)
        - Camera (Vision)
        
        **Bộ truyền động (Actuators):**
        - Động cơ DC: Quay liên tục
        - Servo motor: Quay góc chính xác (0-180°)
        - Stepper motor: Quay từng bước
        - Solenoid: Chuyển động tuyến tính
        
        **Vi điều khiển:**
        - Arduino: Dễ học, cộng đồng lớn
        - Raspberry Pi: Máy tính mini
        - ESP32: Có WiFi/Bluetooth tích hợp
        
        **3. Ví dụ code Arduino:**
        ```cpp
        // Nhấp nháy LED
        void setup() {
            pinMode(13, OUTPUT);
        }
        
        void loop() {
            digitalWrite(13, HIGH);
            delay(1000);
            digitalWrite(13, LOW);
            delay(1000);
        }
        
        // Điều khiển servo
        #include <Servo.h>
        Servo myServo;
        
        void setup() {
            myServo.attach(9);
        }
        
        void loop() {
            myServo.write(0);
            delay(1000);
            myServo.write(90);
            delay(1000);
            myServo.write(180);
            delay(1000);
        }
        ```
        
        **4. Các loại robot:**
        - **Robot di động**: Tự di chuyển (xe tự hành)
        - **Robot công nghiệp**: Lắp ráp, hàn
        - **Robot dịch vụ**: Hỗ trợ con người
        - **Drone**: Bay được
        
        **5. Thuật toán Robot:**
        - Tránh vật cản
        - Theo đường line
        - SLAM: Vẽ bản đồ và định vị
        - PID: Điều khiển chính xác
        
        **6. Dự án thực hành:**
        - Xe tránh vật cản
        - Robot theo line
        - Cánh tay robot
        - Hệ thống tưới cây tự động
        """,
        "resources": [
            "📚 Sách: 'Arduino cho người mới bắt đầu'",
            "🎥 YouTube: 'Paul McWhorter Arduino', 'James Bruton'",
            "🔗 Website: arduino.cc, raspberrypi.org"
        ]
    },
    
    "Internet of Things (IoT)": {
        "icon": "📡",
        "content": """
        ### Giới thiệu về Internet of Things
        
        **1. IoT là gì?**
        - Mạng lưới thiết bị kết nối internet
        - Thu thập và trao đổi dữ liệu
        - Ví dụ: Nhà thông minh, smartwatch
        
        **2. Kiến trúc IoT:**
        
        **Layer 1 - Thiết bị:**
        - Cảm biến thu thập dữ liệu
        - Arduino, ESP8266, ESP32
        
        **Layer 2 - Gateway:**
        - Kết nối thiết bị với cloud
        - Raspberry Pi, router
        
        **Layer 3 - Cloud:**
        - Lưu trữ và xử lý dữ liệu
        - AWS IoT, Google Cloud IoT
        
        **Layer 4 - Ứng dụng:**
        - Dashboard, mobile app
        - Hiển thị và điều khiển
        
        **3. Giao thức IoT:**
        
        **MQTT:**
        - Nhẹ, tiết kiệm băng thông
        - Mô hình Publish/Subscribe
        
        **HTTP/HTTPS:**
        - RESTful API
        - Request/Response
        
        **CoAP:**
        - Tối ưu cho thiết bị hạn chế
        - Giống HTTP nhưng nhẹ hơn
        
        **4. Ví dụ dự án IoT:**
        
        **Hệ thống giám sát nhiệt độ:**
        ```cpp
        #include <WiFi.h>
        #include <PubSubClient.h>
        
        const char* ssid = "WiFi_Name";
        const char* password = "WiFi_Pass";
        const char* mqtt_server = "broker.hivemq.com";
        
        WiFiClient espClient;
        PubSubClient client(espClient);
        
        void setup() {
            Serial.begin(115200);
            WiFi.begin(ssid, password);
            client.setServer(mqtt_server, 1883);
        }
        
        void loop() {
            float temp = readTemperature();
            String payload = String(temp);
            client.publish("home/temperature", payload.c_str());
            delay(5000);
        }
        ```
        
        **5. Nền tảng IoT phổ biến:**
        - **Blynk**: Tạo app mobile nhanh
        - **ThingSpeak**: Lưu trữ và hiển thị dữ liệu
        - **Firebase**: Database realtime
        - **AWS IoT**: Giải pháp enterprise
        
        **6. Bảo mật IoT:**
        - Mã hóa truyền thông (TLS/SSL)
        - Xác thực thiết bị
        - Cập nhật firmware
        - Firewall và VPN
        
        **7. Ứng dụng thực tế:**
        - Smart Home: Đèn, điều hòa, camera
        - Nông nghiệp: Tưới tự động, giám sát đất
        - Y tế: Theo dõi sức khỏe
        - Công nghiệp: Giám sát máy móc
        """,
        "resources": [
            "📚 Sách: 'IoT Fundamentals'",
            "🎥 YouTube: 'Random Nerd Tutorials'",
            "🔗 Website: iot.electronicsforu.com"
        ]
    },
    
    "Trí tuệ nhân tạo (AI)": {
        "icon": "🧠",
        "content": """
        ### Giới thiệu về Trí tuệ Nhân tạo
        
        **1. AI là gì?**
        - Máy tính có khả năng học hỏi và tư duy
        - Mô phỏng trí thông minh con người
        
        **2. Các nhánh của AI:**
        
        **Machine Learning:**
        - Máy học từ dữ liệu
        - Supervised, Unsupervised, Reinforcement
        
        **Deep Learning:**
        - Mạng neural nhiều lớp
        - CNN: Xử lý ảnh
        - RNN/LSTM: Xử lý chuỗi
        
        **Natural Language Processing:**
        - Xử lý ngôn ngữ tự nhiên
        - Chatbot, dịch máy, phân tích cảm xúc
        
        **Computer Vision:**
        - Nhận diện ảnh, video
        - Face detection, object detection
        
        **3. Ví dụ code Machine Learning:**
        ```python
        from sklearn.tree import DecisionTreeClassifier
        import numpy as np
        
        # Dữ liệu: [chiều cao, cân nặng]
        X = [[180, 80], [165, 55], [170, 65], [175, 70]]
        y = ['nam', 'nữ', 'nữ', 'nam']  # Nhãn
        
        # Huấn luyện mô hình
        model = DecisionTreeClassifier()
        model.fit(X, y)
        
        # Dự đoán
        new_data = [[172, 68]]
        prediction = model.predict(new_data)
        print(f"Dự đoán: {prediction}")
        ```
        
        **4. Thư viện phổ biến:**
        
        **Python:**
        - TensorFlow: Framework AI mạnh mẽ
        - PyTorch: Linh hoạt cho nghiên cứu
        - scikit-learn: ML truyền thống
        - OpenCV: Xử lý ảnh
        - NLTK: Xử lý ngôn ngữ
        
        **5. Các thuật toán cơ bản:**
        
        **Linear Regression:**
        - Dự đoán giá trị liên tục
        - y = mx + b
        
        **Decision Tree:**
        - Cây quyết định
        - Phân loại dựa trên điều kiện
        
        **Neural Network:**
        - Input layer → Hidden layers → Output layer
        - Activation functions: ReLU, Sigmoid
        
        **6. Ứng dụng AI:**
        - **Nhận diện khuôn mặt**: Mở khóa điện thoại
        - **Trợ lý ảo**: Siri, Google Assistant
        - **Xe tự lái**: Tesla Autopilot
        - **Đề xuất**: Netflix, YouTube
        - **Dịch máy**: Google Translate
        - **Y tế**: Chẩn đoán bệnh từ ảnh
        
        **7. Dự án thực hành:**
        - Phân loại hoa Iris
        - Nhận diện chữ số viết tay (MNIST)
        - Chatbot đơn giản
        - Dự đoán giá nhà
        """,
        "resources": [
            "📚 Sách: 'Machine Learning cơ bản'",
            "🎥 YouTube: 'Sentdex', '3Blue1Brown'",
            "🔗 Website: kaggle.com, coursera.org"
        ]
    }
}

# Câu hỏi trắc nghiệm
QUIZ_QUESTIONS = {
    "Cơ bản về Điện tử": [
        {
            "question": "Định luật Ohm là gì?",
            "options": ["V = I × R", "V = I / R", "V = I + R", "V = I - R"],
            "answer": 0
        },
        {
            "question": "Đơn vị của điện trở là gì?",
            "options": ["Ampere", "Volt", "Ohm", "Watt"],
            "answer": 2
        },
        {
            "question": "Transistor có mấy chân?",
            "options": ["2 chân", "3 chân", "4 chân", "5 chân"],
            "answer": 1
        },
        {
            "question": "Thiết bị nào cho phép dòng điện chạy một chiều?",
            "options": ["Điện trở", "Tụ điện", "Điốt", "Cuộn cảm"],
            "answer": 2
        }
    ],
    "Lập trình cơ bản": [
        {
            "question": "Ngôn ngữ nào dễ học nhất cho người mới?",
            "options": ["C++", "Python", "Assembly", "Java"],
            "answer": 1
        },
        {
            "question": "Vòng lặp nào có số lần lặp xác định?",
            "options": ["While", "Do-While", "For", "Tất cả đều sai"],
            "answer": 2
        },
        {
            "question": "Hàm (Function) có tác dụng gì?",
            "options": ["Lưu trữ dữ liệu", "Tái sử dụng code", "Khai báo biến", "In ra màn hình"],
            "answer": 1
        },
        {
            "question": "Kiểu dữ liệu nào lưu trữ text?",
            "options": ["int", "float", "string", "boolean"],
            "answer": 2
        }
    ],
    "Mạng máy tính": [
        {
            "question": "IP là viết tắt của gì?",
            "options": ["Internet Protocol", "Internal Program", "Input Process", "Install Package"],
            "answer": 0
        },
        {
            "question": "Mô hình OSI có mấy lớp?",
            "options": ["5 lớp", "6 lớp", "7 lớp", "8 lớp"],
            "answer": 2
        },
        {
            "question": "Giao thức nào dùng cho web?",
            "options": ["FTP", "HTTP", "SMTP", "DNS"],
            "answer": 1
        },
        {
            "question": "Thiết bị nào định tuyến giữa các mạng?",
            "options": ["Switch", "Hub", "Router", "Modem"],
            "answer": 2
        }
    ],
    "Cơ học Robot": [
        {
            "question": "Arduino sử dụng ngôn ngữ nào?",
            "options": ["Python", "Java", "C/C++", "JavaScript"],
            "answer": 2
        },
        {
            "question": "Servo motor quay được bao nhiêu độ?",
            "options": ["0-90°", "0-180°", "0-270°", "0-360°"],
            "answer": 1
        },
        {
            "question": "Cảm biến nào đo khoảng cách?",
            "options": ["LDR", "PIR", "Ultrasonic", "LM35"],
            "answer": 2
        },
        {
            "question": "Pin nào được dùng để điều khiển LED trên Arduino?",
            "options": ["Pin 0", "Pin 13", "Pin A0", "Pin GND"],
            "answer": 1
        }
    ],
    "Internet of Things (IoT)": [
        {
            "question": "IoT là viết tắt của gì?",
            "options": ["Internet of Things", "Internal of Technology", "Install of Tools", "Input of Time"],
            "answer": 0
        },
        {
            "question": "Giao thức nào nhẹ nhất cho IoT?",
            "options": ["HTTP", "FTP", "MQTT", "SMTP"],
            "answer": 2
        },
        {
            "question": "ESP32 có tính năng gì đặc biệt?",
            "options": ["Có màn hình", "Có WiFi/Bluetooth", "Chạy rất nhanh", "Giá rất rẻ"],
            "answer": 1
        },
        {
            "question": "Nền tảng nào tốt cho IoT mobile app?",
            "options": ["Blynk", "Facebook", "Twitter", "Instagram"],
            "answer": 0
        }
    ],
    "Trí tuệ nhân tạo (AI)": [
        {
            "question": "AI là viết tắt của gì?",
            "options": ["Artificial Intelligence", "Automatic Information", "Advanced Internet", "Active Install"],
            "answer": 0
        },
        {
            "question": "Thư viện Python nào dùng cho Machine Learning?",
            "options": ["NumPy", "Pandas", "scikit-learn", "Matplotlib"],
            "answer": 2
        },
        {
            "question": "CNN dùng để xử lý gì?",
            "options": ["Âm thanh", "Ảnh", "Text", "Video"],
            "answer": 1
        },
        {
            "question": "Dataset MNIST chứa gì?",
            "options": ["Ảnh mèo", "Ảnh chó", "Chữ số viết tay", "Khuôn mặt"],
            "answer": 2
        }
    ]
}

# Sidebar - Menu điều hướng
with st.sidebar:
    st.markdown("### 📚 Menu học tập")
    st.markdown("---")
    
    mode = st.radio("Chọn chế độ:", ["📖 Học bài", "✏️ Kiểm tra", "📊 Tiến độ"])
    
    st.markdown("---")
    st.markdown("### 📈 Thống kê của bạn")
    st.info(f"✅ Đã hoàn thành: {len(st.session_state.completed_lessons)}/{len(LESSONS)} bài")
    
    if st.session_state.quiz_score > 0:
        st.success(f"🏆 Điểm quiz: {st.session_state.quiz_score}")

# Chế độ học bài
if mode == "📖 Học bài":
    st.markdown("## 📖 Chọn bài học")
    
    # Hiển thị các bài học dạng card
    cols = st.columns(2)
    for idx, (lesson_name, lesson_data) in enumerate(LESSONS.items()):
        with cols[idx % 2]:
            is_completed = lesson_name in st.session_state.completed_lessons
            status = "✅" if is_completed else "📝"
            
            if st.button(f"{lesson_data['icon']} {status} {lesson_name}", key=f"btn_{lesson_name}", use_container_width=True):
                st.session_state.current_lesson = lesson_name
    
    # Hiển thị nội dung bài học
    if st.session_state.current_lesson:
        lesson_name = st.session_state.current_lesson
        lesson_data = LESSONS[lesson_name]
        
        st.markdown("---")
        st.markdown(f"## {lesson_data['icon']} {lesson_name}")
        
        # Nội dung bài học
        st.markdown(lesson_data['content'])
        
        # Tài liệu tham khảo
        st.markdown("### 📚 Tài liệu tham khảo")
        for resource in lesson_data['resources']:
            st.markdown(f"- {resource}")
        
        # Nút đánh dấu hoàn thành
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("✅ Hoàn thành bài học"):
                if lesson_name not in st.session_state.completed_lessons:
                    st.session_state.completed_lessons.append(lesson_name)
                    st.success("🎉 Chúc mừng! Bạn đã hoàn thành bài học này!")
                    st.balloons()
                else:
                    st.info("Bạn đã hoàn thành bài này rồi!")

# Chế độ kiểm tra
elif mode == "✏️ Kiểm tra":
    st.markdown("## ✏️ Kiểm tra kiến thức")
    
    # Chọn chủ đề
    topic = st.selectbox("Chọn chủ đề để kiểm tra:", list(QUIZ_QUESTIONS.keys()))
    
    if st.button("🎯 Bắt đầu kiểm tra", type="primary"):
        st.session_state.quiz_answers = {}
        st.rerun()
    
    if topic:
        questions = QUIZ_QUESTIONS[topic]
        
        st.markdown(f"### 📝 Bài kiểm tra: {topic}")
        st.markdown(f"Số câu hỏi: **{len(questions)}**")
        st.markdown("---")
        
        # Hiển thị câu hỏi
        user_answers = []
        for i, q in enumerate(questions):
            st.markdown(f"**Câu {i+1}: {q['question']}**")
            answer = st.radio(
                "Chọn đáp án:",
                q['options'],
                key=f"q_{topic}_{i}",
                index=None
            )
            user_answers.append(answer)
            st.markdown("---")
        
        # Nộp bài
        if st.button("📤 Nộp bài", type="primary"):
            score = 0
            total = len(questions)
            
            st.markdown("### 📊 Kết quả")
            
            for i, q in enumerate(questions):
                correct_answer = q['options'][q['answer']]
                user_answer = user_answers[i]
                
                if user_answer == correct_answer:
                    score += 1
                    st.markdown(f"✅ **Câu {i+1}**: Đúng!")
                else:
                    st.markdown(f"❌ **Câu {i+1}**: Sai!")
                    st.markdown(f"   - Đáp án của bạn: {user_answer if user_answer else 'Chưa chọn'}")
                    st.markdown(f"   - Đáp án đúng: {correct_answer}")
            
            percentage = (score / total) * 100
            st.markdown("---")
            
            if percentage >= 80:
                st.success(f"🎉 Xuất sắc! Bạn đạt {score}/{total} điểm ({percentage:.0f}%)")
                st.balloons()
            elif percentage >= 60:
                st.info(f"👍 Khá tốt! Bạn đạt {score}/{total} điểm ({percentage:.0f}%)")
            else:
                st.warning(f"💪 Cố gắng thêm! Bạn đạt {score}/{total} điểm ({percentage:.0f}%)")
            
            st.session_state.quiz_score += score

# Chế độ tiến độ
elif mode == "📊 Tiến độ":
    st.markdown("## 📊 Tiến độ học tập của bạn")
    
    # Thống kê tổng quan
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📚 Tổng số bài", len(LESSONS))
    
    with col2:
        completed = len(st.session_state.completed_lessons)
        st.metric("✅ Đã hoàn thành", completed)
    
    with col3:
        remaining = len(LESSONS) - completed
        st.metric("📝 Còn lại", remaining)
    
    # Progress bar
    progress = completed / len(LESSONS) if len(LESSONS) > 0 else 0
    st.progress(progress)
    st.markdown(f"**Tiến độ: {progress*100:.1f}%**")
    
    st.markdown("---")
    
    # Chi tiết từng bài
    st.markdown("### 📋 Chi tiết các bài học")
    
    for lesson_name, lesson_data in LESSONS.items():
        is_completed = lesson_name in st.session_state.completed_lessons
        status = "✅ Đã hoàn thành" if is_completed else "⏳ Chưa hoàn thành"
        color = "green" if is_completed else "orange"
        
        st.markdown(f"**{lesson_data['icon']} {lesson_name}**: :{color}[{status}]")
    
    st.markdown("---")
    
    # Điểm quiz
    st.markdown("### 🏆 Điểm số")
    st.info(f"Tổng điểm quiz: **{st.session_state.quiz_score}** điểm")
    
    # Thành tích
    st.markdown("### 🎖️ Thành tích")
    
    achievements = []
    if completed >= 1:
        achievements.append("🌟 Người mới bắt đầu - Hoàn thành bài đầu tiên")
    if completed >= 3:
        achievements.append("⭐ Học sinh chăm chỉ - Hoàn thành 3 bài")
    if completed >= len(LESSONS):
        achievements.append("🏆 Bậc thầy - Hoàn thành tất cả bài học")
    if st.session_state.quiz_score >= 10:
        achievements.append("🎯 Cao thủ - Đạt 10+ điểm quiz")
    
    if achievements:
        for achievement in achievements:
            st.success(achievement)
    else:
        st.info("Hãy hoàn thành bài học để mở khóa thành tích!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888;'>
    <p>💡 <b>Tool học tập Công nghệ Kỹ thuật</b></p>
    <p>Học tập hiệu quả - Kiến thức vững chắc - Tương lai rộng mở</p>
    <p><i>Phát triển bởi hien © 2024</i></p>
</div>
""", unsafe_allow_html=True)
