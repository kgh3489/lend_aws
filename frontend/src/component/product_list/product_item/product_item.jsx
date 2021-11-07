import React from 'react';
import { useHistory } from 'react-router-dom';
import styles from './product_item.module.css';

const Product = ({product}) => {
        
    const history = useHistory();

    const onProductClick = () => {
        history.push({
            pathname: `product/${product.id}`,
            props: product.id
        
        })
    }



    return (
        <div className={styles.product_item}>
            <div className={styles.container} onClick={onProductClick}>
                <div className={styles.imagesec}>
                    <img className={styles.bycle_img} src={product.product_img} alt="" />
                </div>
                <div className={styles.descsec}>
                    <div className={styles.product_title}>
                        <span>{product.product_name}</span>
                    </div>
                    <div className={styles.product_desc}>
                        <span>{product.product_detail}</span>
                    </div>
                    {/* <span className={styles.product_seller}>판매자 : {product.member} </span> */}
                    <div className={styles.product_price}>
                        <span>가격: 시간당 {product.product_lend_h}원 / </span>
                        <span>일당 {product.product_lend_d}원</span>
                    </div>
                </div>
            </div>
        </div>
    )
};

export default Product;