import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Company } from './company';
import { Vacancy } from "./vacancy";

interface Credentials {
  username: string;
  password: string;
}

@Injectable({
  providedIn: 'root'
})
export class DataService {
  apiUrl = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) { }

  logIn(credentials : Credentials) {
    return this.http.post<any>(`${this.apiUrl}admin/`, credentials);
  }

  getCompanies() {
    return this.http.get<Company[]>(`${this.apiUrl}api/companies`);
  }

  getCompany(id: number) {
    return this.http.get<Company>(`${this.apiUrl}companies/${id}`);
  }

  getVacanciesByCompany(id: number) {
    return this.http.get<Vacancy[]>(`${this.apiUrl}companies/${id}/vacancies`);
  }

  getVacancies() {
    return this.http.get<Vacancy[]>(`${this.apiUrl}vacancies`);
  }

  getVacancy(id: number) {
    return this.http.get<Vacancy>(`${this.apiUrl}vacancies/${id}`);
  }

  getTopTenVacancies() {
    return this.http.get<Vacancy[]>(`${this.apiUrl}vacancies/top_ten`);
  }
}
