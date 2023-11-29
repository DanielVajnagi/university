// news.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css'],
})
export class NewsComponent {
  newsList: News[] = [
    { title: 'Заголовок новини 1', content: 'Важлива інформація про подію 1.' },
    { title: 'Заголовок новини 2', content: 'Інформація про подію 2, що трапилася недавно.' },
    { title: 'Заголовок новини 3', content: 'Останні новини та оновлення в області.' },
  ];

  constructor() {}

  // Інші методи та логіка можуть бути додані тут
}

interface News {
  title: string;
  content: string;
}
