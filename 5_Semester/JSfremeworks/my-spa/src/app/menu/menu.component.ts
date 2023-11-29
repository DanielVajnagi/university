// menu.component.ts
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css'],
})
export class MenuComponent implements OnInit {
  isAuthenticated: boolean = false;

  constructor(private router: Router) {}

  ngOnInit() {
    this.isAuthenticated = localStorage.getItem('authenticated') === 'true';
  }

  logout() {
    localStorage.removeItem('authenticated');
    this.router.navigate(['/login']);
  }

  isLoginPage(): boolean {
    return this.router.url === '/login';
  }
}
