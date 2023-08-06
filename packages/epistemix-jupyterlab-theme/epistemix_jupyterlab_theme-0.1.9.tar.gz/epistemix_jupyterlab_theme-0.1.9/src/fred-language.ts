import { JupyterFrontEnd } from '@jupyterlab/application';
import { LabIcon } from '@jupyterlab/ui-components';

const FRED = {
  name: 'fred',
  displayName: 'FRED',
  extensions: ['fred', 'fredmod'],
  mimetype: 'application/x-fred',
  icon: new LabIcon({
    name: 'fredIcon',
    svgstr: `<svg xmlns="http://www.w3.org/2000/svg" width="320" height="320" viewBox="0 0 320 320">
      <g class="jp-icon-selectable">
        <path d="M225.3 143.6v32.8h-91.8v32.8H245V242H81v-98.4h144.3ZM81 110.8V78h157.4v32.8H81Z" fill="#FFF"/>
      </g>
    </svg>`
  })
};

function registerFREDFileType(app: JupyterFrontEnd) {
  app.docRegistry.addFileType({
    name: FRED.name,
    displayName: FRED.displayName,
    extensions: FRED.extensions.map(m => `.${m}`),
    mimeTypes: [FRED.mimetype],
    icon: FRED.icon,
    iconLabel: FRED.displayName
  });
}

function registerFREDWithCodeMirror(codeMirror: any) {
  (codeMirror as any).defineSimpleMode(FRED.name, {
    // The start state contains the rules that are initially used
    start: [
      {
        regex: /\bcomment\s*{/,
        token: 'comment',
        next: 'comment'
      },
      {
        regex:
          /^\d{4}-(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-(?:0[1-9]|[12][0-9]|3[01])$/,
        token: 'date'
      },
      {
        regex:
          /\b(?:if|state|condition|then|with|simulation|startup|variables|place|network)\b/,
        token: 'keyword.control'
      },
      {
        regex: /\b(agent|shared)( )(list|numeric|table|list_table)\b/,
        token: ['keyword.vartype', null, 'keyword.vartype']
      },
      {
        regex:
          /\b(?:Apr|Aug|Dec|Feb|Fri|FRED|Jan|Jul|Jun|Mar|May|Mon|Nov|Oct|R0|R0_a|R0_b|Sat|Sep|Sun|Thu|Tue|Var|Wed|abs|add|group_start_state|african_american|age|age_in_days|age_in_months|age_in_weeks|age_in_years|alaska_native|american_indian|asian|at|base_type|bernoulli|binomial|birth_year|boarder|can_transmit_|cauchy|chi_squared|child|college_student|comment|condition_to_import|condition_to_transmit|contact_count_for_|contact_rate_for_|contacts|cos|date|date_range|day_of_month|day_of_week|day_of_year|density_contact_prob|density_contact_prob_for_|density_transmission|density_transmission_for_|deterministic_contact_for_|dist|distance|div|enable_health_records|enable_visualization|end_date|epi_week|epi_year|eq|equal|exp|exponential|exposed_externally|exposed_in|exposed_state|extreme_value|female|filter|fisher_f|fisher_t|foster_child|fred|gamma|geometric|gompertz|grandchild|gt|gte|has_administrator|has_been_closed|hawaiian_native|host|hosts|hour|household_relationship|householder|housemate|id|id_of_source_of_|import_start_state|in|in_law|include|infant|inlinks|institutionalized_group_quarters_pop|is_absent|is_at|is_connected_from|is_connected_to|is_dormant|is_host|is_in_list|is_member|is_open|is_undirected|join|list|list_size_of_ListVar|locations|log|lognormal|lognormal_std|lt|lte|male|max|max_size|member|military|min|min_partitions|mod|module|month|mult|multiple_race|my|my_list|negative_binomial|negbinomial|neq|network|new|next|noninstitutionalized_group_quarters_pop|normal|not|now|number_of_children|nursing_home_resident|open|other_non_relative|other_race|other_relative|outlinks|output|parent|partition|partition_basis|partition_max_age|partition_min_age|partition_size|partner|place|place_type_to_transmit|poisson|pool|pow|pref|preschool|print_interval|prisoner|profile|quit|race|range|retired|same_age_bias|select|set|set_list|sex|sibling|sim_day|sim_mon|sim_run|sim_step|sim_week|sim_year|simple_factor|sin|spouse|start_date|start_hosting|starts_at_hour_|states|step|student|student_t|sub|sus|susceptibility_to_|teacher|time_since_entering_|today|trans|transmissibility|transmissibility_for_|transmissibility_of_|transmissible_networks|transmissiion_network|transmission_mode|transmissions_of_|tribal|unemployed|uniform|unknown_race|use|value|visualize|visualize_place_type|wait|was_exposed_externally|was_exposed_in|weekend_worker|weibull|white|worker|year|variables|parameters|prob|default|set_state|absent|import_count|nprob|meta_start_state|start_state|site|length|ask|push|lookup|lookup_list|debug_variable|range_list|size|sum|round|present|last|until)\b/,
        token: 'string'
      },
      {
        regex: /(\.)(default_value|output)/,
        token: [null, 'string']
      },
      {
        regex: /(?:Excluded|Population)/,
        token: 'atom'
      },
      {
        regex: /0x[a-f\d]+|[-+]?(?:\.\d+|\d+\.?\d*)(?:e[-+]?\d+)?/i,
        token: 'number'
      },
      {
        regex: /[{[(]/,
        indent: true
      },
      {
        regex: /[}\])]/,
        dedent: true
      },
      {
        regex: /#.*$/,
        token: 'comment'
      },
      {
        regex: /[-+/*=<>!]+/,
        token: 'operator'
      }
    ],

    // The multi-line comment state.
    comment: [
      {
        regex: /.*?}/,
        token: 'comment',
        next: 'start'
      },
      {
        regex: /.*/,
        token: 'comment'
      }
    ],

    // The meta property contains global information about the mode. It
    // can contain properties like lineComment, which are supported by
    // all modes, and also directives like dontIndentStates, which are
    // specific to simple modes.
    meta: {
      dontIndentStates: ['comment'],
      lineComment: '#'
    }
  });

  (codeMirror as any).defineMIME(FRED.mimetype, FRED.name);

  (codeMirror as any).modeInfo.push({
    name: FRED.displayName,
    mime: FRED.mimetype,
    mode: FRED.name,
    ext: FRED.extensions
  });
}

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
export function registerFRED(app: JupyterFrontEnd, codeMirror: any): void {
  registerFREDFileType(app);
  registerFREDWithCodeMirror(codeMirror);
}
