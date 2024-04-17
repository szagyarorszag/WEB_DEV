import { Routes } from '@angular/router';
import { CompaniesComponent } from './companies/companies.component';
import { VacanciesComponent } from './vacancies/vacancies.component';
import { UserComponent} from "./user/user.component";

export const routes: Routes = [
  { path: 'companies', component: CompaniesComponent },
  { path: 'vacancies', component: VacanciesComponent },
  { path: 'user', component: UserComponent},
];

