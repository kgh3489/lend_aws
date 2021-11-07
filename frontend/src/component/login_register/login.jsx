import React, {useEffect, useState} from 'react';
import { useHistory, useLocation } from 'react-router-dom';
import styles from './login.module.css';
import { KakaoAuth } from '../../service/kakaoAuth';
import axios from 'axios';

const Login = (props) => {
    
    /* 컴포넌트 스위칭 */
    const history = useHistory();
    
    const goToHome = () => {
        history.push({
            pathname: "/"
        })
    }
    const goToSignUp = () => {
        history.push({
            pathname: "/signUp"
        })
    }

    const[loginData, setLoginData] = useState({
        "username": '',
        "password": '',
    })

    
    // 네이버 로그인
    const {naver} = window;
    const initializeNaverLogin = () => {
        const naverLogin = new naver.LoginWithNaverId({
            clientId: "aLUPHGNIXs0WoC2mVxqX",
            callbackUrl: "http://localhost:3000/login", 
            isPopup: false, // popup 형식으로 띄울것인지 설정
            loginButton: { color: 'white', type: 3, height: '55' }, //버튼의 스타일, 타입, 크기를 지정
        });
        naverLogin.init();
    };

    const location = useLocation();

    const getNaverToken = () => {
        if (!location.hash) return;
        const token = location.hash.split('=')[1].split('&')[0];
        console.log(token);
    };

    useEffect(() => {
        initializeNaverLogin();
        getNaverToken();
    });


    const handleLogin = (e) => {
        e.preventDefault();

        const arr = Object.entries(loginData);
        for(let i = 0; i< arr.length; i++) {
            if(arr[i][1] === "") {
                return alert(`${arr[i][0]} 을(를) 입력해주세요.`);
            }
        }
        axios({
            method: 'post',
            url: '/user/login/',
            data: JSON.stringify({
                username: loginData.username,
                password: loginData.password,
            }),
            headers: {
                "Content-Type": "application/json",
            }

        })
        .then(response => {
            console.log(response);
            console.log('로그인 성공')
            localStorage.setItem('ACCESS_TOKEN',response.data.token);
            goToHome();
        })
        .catch(error => {
            alert('아이디와 비밀번호를 확인해주세요.')
        })
    }

    const handleChange = (e) => { //요소에 변화가 생기면 실행
        setLoginData({
            ...loginData,
            [e.target.name]: e.target.value,
        })
    }


    
    

    return (
        <div className={styles.container}>
            <div className={styles.header}>
                <button className={styles.gotoHome} onClick={goToHome}><i className="fas fa-arrow-left"></i></button>
            </div>
            <div className={styles.mainContent}>
                <div className={styles.banner}>
                    <img className={styles.logo} src={process.env.PUBLIC_URL + "/static/logo.png"} alt="logo" />
                </div>
                <div className={styles.form}>
                    <div className={styles.form_group}>
                        <label htmlFor="username">아이디</label>
                        <input type="text" name="username" placeholder="아이디를 입력해주세요" value={loginData.username || ""} onChange={handleChange}/>
                    </div>
                    <div className={styles.form_group}>
                        <label htmlFor="password">비밀번호</label>
                        <input type="password" name="password" placeholder="비밀번호를 입력해주세요" value={loginData.password || ""} onChange={handleChange}/>
                    </div>
                </div>
                <div className={styles.btns}>
                    <button className={styles.login_btn} onClick={handleLogin}>로그인</button>
                    <button className={styles.register_btn} onClick={goToSignUp}>회원가입</button>
                </div>
                <div className={styles.loginSeperate}>
                    <hr />
                </div>
                <div className={styles.login_sns}>
                    <div id="naverIdLogin" className={styles.login_sns}></div>  
                    <a href={KakaoAuth}>
                        <button className={styles.login_sns}>
                            <img src="/static/kakao_login.png" alt="kakao_login" />
                        </button>
                    </a>
                </div>
            </div>
            
        </div>
    )
};

export default Login;



/* 
    // 콜백URL, 클라이언트 아이디 대입
    const {naver} = window;

    const Naver = () => {
        const naverLogin = new naver.LoginWithNaverId({
            clientId: aLUPHGNIXs0WoC2mVxqX,
            callbackUrl: "http://localhost:3000/login",
            isPopup: true,
            loginButton: {
                color: 'green',
                type: 3,
                height: '50'
            }
        });
        naverLogin.init();
    };
    // 로직
    const UserProfile = () => {
        window.location.href.includes('access_token') && GetUser();
        function GetUser() {
            const location = window.location.href.split('=')[1];
            const form_data = new FormData();
        
            const item:any = {
                token: location.split('&')[0],
            };
            for (const key in item) {
                form_data.append(key, item[key]);
            }
            fetch(${""}, {
                method: 'POST',
                body: form_data,
            }).then((res) => res.json())
                .then((resjson) => {
                if (resjson.responseCode == '403') {
                    // 사용자가 없으니 회원가입 창으로
                } else if (resjson.responseCode == '200') {
                    // 로그인이 되었으니 이 후 process 로 이동
                }
                }).catch((err) => console.log(err));
        }
    };
    // 실행
    const NaverLogin = () => {
        Naver();
        UserProfile();
    }
 */