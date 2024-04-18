import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Company } from "../company";
import { Vacancy} from "../vacancy";

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit {
  companies?: Company[];
  vacancies?: Vacancy[];
  selectedCompany?: Company;



  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.getCompanies();
  }

  getCompanies() {
    this.dataService.getCompanies().subscribe(companies  => this.companies = companies );
  }

  getCompany(company: Company): void {
    this.selectedCompany = company;
    this.getVacanciesByCompany(company.id);
  }

  getVacanciesByCompany(id: number): void {
    this.dataService.getVacanciesByCompany(id).subscribe(vacancies => this.vacancies = vacancies);
  }
}
