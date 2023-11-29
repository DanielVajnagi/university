// profile.component.ts
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css'],
})
export class ProfileComponent implements OnInit {
  isAuthenticated: boolean = false;

  ngOnInit() {
    // Перевірка авторизації при завантаженні компонента
    this.isAuthenticated = localStorage.getItem('authenticated') === 'true';
  }
}
