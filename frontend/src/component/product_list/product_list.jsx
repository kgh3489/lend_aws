import React, { useRef } from 'react';
import styles from './product_list.module.css';
import Product from './product_item/product_item';

const ProductList = ({products, filteredData, setFilteredData, searchProducts}) => {

    

    //필터 기능
    const filterRef = useRef();

    const filterHandler = () => {
        filterRef.current.style.display = 'block'
    }

    const filterMTV = () => {
        let filteredM = products.filter((type) => {
            return type.product_type === 'MTV';
            });
            console.log(filteredM);
            setFilteredData(filteredM);
        filterRef.current.style.display = 'none';
    }
    const filterHybrid = () => {
        let filteredH = products.filter((type) => {
            return type.product_type === '하이브리드';
            });
            console.log(filteredH);
            setFilteredData(filteredH);
        filterRef.current.style.display = 'none';
    }
    const filterRoad = () => {
        let filteredR = products.filter((type) => {
            return type.product_type === '로드';
            });
            console.log(filteredR);
            setFilteredData(filteredR);
        filterRef.current.style.display = 'none';
    }

    return (
        <section className={styles.product_list}>
            <button onClick={filterHandler} className={styles.filterBtn}><i className="fas fa-filter"></i></button>
            <div ref={filterRef} className={styles.filterBox}>
                <div className={styles.bikeBox}>
                    <button onClick={filterMTV} className={styles.bikeBtn}>MTV</button>
                    <button onClick={filterHybrid} className={styles.bikeBtn}>하이브리드</button>
                    <button onClick={filterRoad} className={styles.bikeBtn}>로드바이크</button>
                </div>
            </div>
            
            {
                filteredData.map(product => 
                    <Product 
                        key={product.id}
                        product={product}
                    />
                )
            }
        </section>
    )


};

export default ProductList;

