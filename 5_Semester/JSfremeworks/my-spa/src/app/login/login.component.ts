import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  username: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private router: Router) {}

  login() {
    if (this.username === 'Admin' && this.password === '12345') {
      localStorage.setItem('authenticated', 'true');
      this.router.navigate(['/profile']);
    } else {
      this.errorMessage = 'Ім\'я користувача або пароль введені не вірно';
    }
  }
}
