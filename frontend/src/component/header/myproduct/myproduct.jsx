import {React, useState, useEffect } from 'react';
import styles from './myproduct.module.css';
import { useHistory } from 'react-router-dom';
import Product from '../../product_list/product_item/product_item';




const MyProdcut = () => {
    
    /* 컴포넌트 스위칭 */
    const history = useHistory();
    
    const goToHome = () => {
        history.push({
            pathname: "/"
        })
    }

    // 해당 회원 토큰마다 상품 지정해서 get 해와야함
    const[products, setProducts] = useState([]);
    
    const loadProducts=() => {
        return fetch(process.env.PUBLIC_URL + "/static/data_sample.json")
        .then(res => res.json())
    }

    const [searchTerm, setSearchTerm] = useState('');

    useEffect(() => {
        loadProducts()
        .then(prod => setProducts(prod["products"]))
    }, [])
    
    return (
        <div className={styles.container}>
            {/* 사용중인 자전거 */}
            <div className={styles.bikeUse}>
                <div className={styles.bikeTitleTop}>
                    <button className={styles.gotoHome} onClick={goToHome}><i className="fas fa-arrow-left"></i></button>
                    <span>대여중인 자전거</span></div>
                <div className={styles.products}>
                    {
                        products.filter(product=> {
                            if (searchTerm === "") {
                                return product
                            } else if (product.product_name.toLowerCase().includes(searchTerm.toLowerCase())) {
                                return product
                            } else if (product.product_description.toLowerCase().includes(searchTerm.toLowerCase())) {
                                return product
                            }
                        }).map(product => 
                            <Product 
                                key={product.id}
                                product={product}
                            />
                        )
                    }
                </div>
            </div>
            {/* 등록한 자전거 */}
            <div className={styles.bikeRent}>
                <div className={styles.bikeTitle}><span>등록중인 자전거</span></div>
                <div className={styles.products}>
                    {
                        products.filter(product=> {
                            if (searchTerm === "") {
                                return product
                            } else if (product.product_name.toLowerCase().includes(searchTerm.toLowerCase())) {
                                return product
                            } else if (product.product_description.toLowerCase().includes(searchTerm.toLowerCase())) {
                                return product
                            }
                        }).map(product => 
                            <Product 
                                key={product.id}
                                product={product}
                            />
                        )
                    }
                </div>
            </div>
        </div>

    );


};

export default MyProdcut;
// className={styles.}

