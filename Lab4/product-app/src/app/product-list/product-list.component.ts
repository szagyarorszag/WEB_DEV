import { Component } from '@angular/core';

import { products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  products = [...products];

  share(link: string, name: string) {
    const message = `Посмотрите ${name}: ${link}`;
    const tgLink = `https://telegram.me/share/url?url=${message}`;
    window.location.href = tgLink;
}
  onNotify(){
    window.alert('You will be notified when the product goes on sale');
  }
}
