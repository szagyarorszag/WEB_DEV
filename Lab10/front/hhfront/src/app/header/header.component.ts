import { Component } from '@angular/core';
import {colors} from "@angular/cli/src/utilities/color";

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {

  protected readonly colors = colors;
}
